import pygame

pygame.init()

font = pygame.font.Font("freesansbold.ttf", 32)


class Scorecard:
    def __init__(self, x, y, surface, text):
        self.x = x
        self.y = y
        self.surface = surface
        self.text = text

    def draw(self):
        text = font.render(self.text, True, "blue")
        self.surface.blit(text, (self.x, self.y))
