import pygame
from data.scenes import SCENES

FONT_COLOR = (255, 255, 255)
BG_COLOR = (20, 20, 20)

class Game:
    def __init__(self, screen): # Inicializálás

        self.full_text = "" # Teljes szöveg
        self.visible_text = "" # Látható szöveg
        self.char_index = 0 # Karakter index

        self.last_char_time = 0 # Utolsó karakter idő
        self.char_delay = 30  # ms / karakter
        self.typing = False # Gépelés állapota

        self.screen = screen # Képernyő beállítása
        self.font = pygame.font.SysFont("Arial", 24) # Betűtípus beállítása
        # current scene ID
        self.current_scene = "start" # Jelenlegi jelenet azonosítója

        # scenes will live here for now
        self.scenes = self.scenes = SCENES # Jelenetek betöltése

        self.choice_rects = [] # Választási téglalapok listája
        self.start_typing()

    def handle_event(self, event): # Esemény kezelése, Mi az a handle_event? A handle_event egy olyan függvény, amely kezeli a különböző eseményeket, például billentyűleütéseket vagy egérkattintásokat a játék során.
        if event.type == pygame.MOUSEBUTTONDOWN and not self.typing: # Egérkattintás esemény és nem gépel
            self.start_typing() # Gépelés indítása

        if event.type == pygame.KEYDOWN: # Billentyű lenyomás esemény
            if event.key == pygame.K_SPACE and self.typing: # Ha a szóköz lenyomva és gépelés folyamatban van
                self.visible_text = self.full_text # Az összes szöveg megjelenítése
                self.typing = False # Gépelés állapotának kikapcsolása
                self.start_typing() # Gépelés indítása


        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = event.pos
            for rect, target in self.choice_rects:
                if rect.collidepoint(mouse_pos):
                    self.current_scene = target

            if rect.collidepoint(mouse_pos):
                self.current_scene = target
                self.start_typing()

    def start_typing(self): # Gépelés indítása
        self.full_text = self.scenes[self.current_scene]["text"] # Teljes szöveg beállítása
        self.visible_text = "" # Látható szöveg törlése
        self.char_index = 0 # Karakter index visszaállítása
        self.last_char_time = pygame.time.get_ticks() # Utolsó karakter idő frissítése
        self.typing = True # Gépelés állapotának beállítása

    def update(self): # Frissítés
        if not self.typing: # Ha nem gépel
            return # Kilépés

        now = pygame.time.get_ticks() # Aktuális idő
        if now - self.last_char_time >= self.char_delay: # Ha elég idő telt el
            self.last_char_time = now # Utolsó karakter idő frissítése
        if self.char_index < len(self.full_text): # Ha van még karakter
            self.visible_text += self.full_text[self.char_index] # Látható szöveg frissítése
            self.char_index += 1 # Karakter index növelése
        else: # Minden karakter megjelenítve
            self.typing = False # Gépelés állapotának beállítása

    def draw(self): # Rajzolás
        self.screen.fill(BG_COLOR)
        self.choice_rects.clear()

        scene = self.scenes[self.current_scene]

        # draw text
        y = 50
        for line in self.visible_text.split("\n"): # Szöveg sorokra bontása
            text_surf = self.font.render(line, True, FONT_COLOR) # Szöveg felület létrehozása
            self.screen.blit(text_surf, (50, y)) # Szöveg kirajzolása
            y += 40 # Sor magasság növelése

        # draw choices
        y += 40
        for text, target in scene["choices"]:
            text_surf = self.font.render(text, True, FONT_COLOR)
            rect = text_surf.get_rect(topleft=(50, y))
            self.screen.blit(text_surf, rect)
            self.choice_rects.append((rect, target))
            y += 40
        if self.typing: # Roviden nem lehet addig kattintani amig nem megy le a dialog-monolog szoveg
            return
