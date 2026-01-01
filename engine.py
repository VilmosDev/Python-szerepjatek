import pygame
from data.scenes import SCENES

FONT_COLOR = (255, 255, 255)
BG_COLOR = (20, 20, 20)

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)

        # current scene ID
        self.current_scene = "start"

        # scenes will live here for now
        self.scenes = self.scenes = SCENES

        self.choice_rects = []

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for rect, target in self.choice_rects:
                if rect.collidepoint(mouse_pos):
                    self.current_scene = target

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.choice_rects.clear()

        scene = self.scenes[self.current_scene]

        # draw text
        y = 50
        for line in scene["text"].split("\n"):
            text_surf = self.font.render(line, True, FONT_COLOR)
            self.screen.blit(text_surf, (50, y))
            y += 40

        # draw choices
        y += 40
        for text, target in scene["choices"]:
            text_surf = self.font.render(text, True, FONT_COLOR)
            rect = text_surf.get_rect(topleft=(50, y))
            self.screen.blit(text_surf, rect)
            self.choice_rects.append((rect, target))
            y += 40
