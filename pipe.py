import pygame


class Pipe:
    def __init__(self, x, y, height, width) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = -2

    def move(self) -> None:
        self.x += self.velocity

    def draw(self, screen) -> None:
        pygame.draw.rect(
            screen, "green", pygame.Rect(self.x, self.y, self.width, self.height)
        )

    def s_update(self,screen):
        self.move()
        self.draw(screen)
