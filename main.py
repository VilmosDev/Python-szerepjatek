import pygame
from engine import Game

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick Story Game")

clock = pygame.time.Clock()
game = Game(screen)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.handle_event(event)

    game.update()
    game.draw()

    pygame.display.flip()

pygame.quit()
