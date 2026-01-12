import pygame
# ez mit jelent? azt hogy a sys modulból csak az exit függvényt importálja.
from sys import exit
import random

# Játék változók

GAME_WiDTH, GAME_HEIGHT = 360, 640

# Bird class, navigációhoz

bird_x = GAME_WiDTH/8 # Bird x pozíciója, a képernyő szélességének 1/8-ánál
bird_y = GAME_HEIGHT/2 # Bird y pozíciója, a képernyő magasságának felénél
bird_width = 34 # Bird szélessége
bird_height = 24 # Bird magassága

class Bird(pygame.Rect): # Bird osztály létrehozása, pygame.Rect osztályból örökölve
    def __init__(self, img): # Konstruktor, img paraméterrel
        pygame.Rect.__init__(self, bird_x, bird_y, bird_width, bird_height) # Szülő osztály konstruktorának meghívása
        self.image = img # Bird képének beállítása

# pipe class
pipe_x = GAME_WiDTH # Pipe x pozíciója, a képernyő szélességénél
pipe_y = 0 # Pipe y pozíciója, 0-nál (felső rész)
pipe_width = 64 # Pipe szélessége
pipe_height = 512 # Pipe magassága

class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, pipe_x, pipe_y, pipe_width, pipe_height)
        self.image = img # Pipe képének beállítása
        self.passed = False # Pipe átment állapotának beállítása

# Háttér
background_image = pygame.image.load('flappybirdbg.png') # Háttér kép !betöltése!
bird_image = pygame.image.load('flappybird.png') # Bird kép !betöltése!
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height)) # Bird kép átméretezése
top_pipe_image = pygame.image.load('toppipe.png') 
top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height))
bottom_pipe_image = pygame.image.load('bottompipe.png')
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height))


def draw(): # Háttér kirajzolása
    window.blit(background_image, (0, 0)) # Háttér kirajzolása a (0,0) pozícióba (bal felső sarok - origin) 
#blit definíciója: egy képet egy másik kép fölé helyezünk

pygame.init() # Pygame inicializálása, elindítása

window = pygame.display.set_mode((GAME_WiDTH, GAME_HEIGHT)) # Ablak létrehozása
pygame.display.set_caption("Flappy Bird") # Ablak címének beállítása

clock = pygame.time.Clock() # Óra létrehozása a képkocka sebesség szabályozásához

create_pipes_timer = pygame.USEREVENT + 0 # Egyedi esemény létrehozása a pipe-ok létrehozásához
pygame.time.set_timer(create_pipes_timer, 1500) # Esemény időzítő beállítása (1500 ms)


# Játék logika
bird = Bird(bird_image) # Bird objektum létrehozása
pipes = [] # Pipe objektumok listája
velocity_x = -2 # Pipe sebessége balra
velocity_y = 0 # Bird fel/le sebessége
gravity = 0.4 # Gravitáció értéke (mennyivel gyorsul a bird lefelé minden frame-ben)
score = 0 # Pontszám inicializálása
game_over = False # Játék vége állapot inicializálása

def draw():
    window.blit(background_image,(0, 0)) # Háttér kirajzolása
    # blit: egy képet egy másik kép fölé helyezünk
    window.blit(bird.image, bird) # Bird kirajzolása a bird.x és bird.y pozícióba

    for pipe in pipes: # Minden pipe kirajzolása
        window.blit(pipe.image, pipe)

    text_string = str(int(score)) # Pontszám szöveggé alakítása
    if game_over:
        text_string = "Game Over! Score: " + text_string # Játék vége szöveg létrehozása pontszámmal

    text_font = pygame.font.SysFont("Comic Sans MS", 50) # Betűtípus létrehozása (alapértelmezett, méret 50)
    text_render = text_font.render(text_string, True, "white") # Szöveg renderelése fehér színnel
    window.blit(text_render, (5,0)) # Szöveg kirajzolása a képernyő tetején középre 

    
def move():
    global velocity_y, score, game_over # Globális változó használata a bird sebességéhez
    velocity_y += gravity # Gravitáció alkalmazása a bird sebességére
    bird.y += velocity_y # Bird mozgatása fel/le
    bird.y = max(bird.y, 0) # Bird y pozíciójának korlátozása (nem mehet felülre a képernyőről)

    if bird.y > GAME_HEIGHT: # Ha a bird leesik az alsó részre
        game_over = True # Játék vége állapot beállítása
        return
    
    for pipe in pipes:
        pipe.x += velocity_x # Pipe-ok mozgatása balra

        if not pipe.passed and bird.x > pipe.x + pipe.width: # Ha a bird áthaladt a pipe-on
            score += 0.5 # Pontszám növelése (fél pont minden pipe-on) Mivel 2 pipe van egy nyíláshoz
            pipe.passed = True # Pipe átment állapotának beállítása

        if bird.colliderect(pipe): # Ha a bird ütközik a pipe-al
            game_over = True # Játék vége állapot beállítása
            return

    # Eltávolítjuk a képernyőről kilépett pipe-okat - Memoria felszabaditasa
    while len(pipes) > 0 and pipes[0].x < -pipe_width: # Ha az első pipe kilépett a képernyőről
        pipes.pop(0) # Eltávolítjuk az első pipe-ot a listából

def create_pipes():
    random_pipe_y = pipe_y - pipe_height/4 - random.random()*(pipe_height/2) # Véletlenszerű y pozíció generálása a felső pipe számára
    opening_space = GAME_HEIGHT / 4 # Nyílás mérete a pipe-ok között


    top_pipe = Pipe(top_pipe_image)
    top_pipe.y = random_pipe_y # Felső pipe y pozíciójának beállítása véletlenszerű értékre
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_image) # Alsó pipe létrehozása
    bottom_pipe.y = top_pipe.y + top_pipe.height + opening_space # Alsó pipe y pozíciójának beállítása a felső pipe y pozíciója + pipe magassága + nyílás mérete
    pipes .append(bottom_pipe)

    print(len(pipes)) # Pipe-ok számának kiírása a konzolra


while True: # Game loop
    for event in pygame.event.get(): # Események kezelése, get visszaadja az összes eseményt
        if event.type == pygame.QUIT: # Kilépés esemény, type - esemény típusa
            pygame.quit()
            exit()

        if event.type == create_pipes_timer and not game_over: # Pipe létrehozás esemény, ha a játék nincs vége
            create_pipes()

        if event.type == pygame.KEYDOWN: # Billentyű lenyomás esemény
            if event.key in (pygame.K_SPACE, pygame.K_x, pygame.K_UP): # Ha a lenyomott billentyű a SPACE, X vagy UP
                velocity_y = -6 # Bird fel sebessége

                # reset game
                if game_over:
                    bird.y = bird_y # Bird y pozíciójának visszaállítása
                    pipes.clear() # Pipe-ok listájának ürítése
                    score = 0 # Pontszám visszaállítása
                    game_over = False # Játék vége állapot visszaállítása


    
    if not game_over:
        move() # Pipe-ok mozgatása
        draw() # Háttér, madár kirajzolása kirajzolása
        pygame.display.update() # Képernyő frissítése
        clock.tick(60) # Képkocka sebesség beállítása (60 FPS)
