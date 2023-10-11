import pygame


class Bird:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10

    def jump(self) -> None:
        self.velocity = self.jump_strength

    def move(self) -> None:
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, screen) -> None:
        pygame.draw.rect(
            screen, "yellow", pygame.Rect(self.x, self.y, self.width, self.height)
        )

    def s_update(self,screen):
        self.move()
        self.draw(screen)

