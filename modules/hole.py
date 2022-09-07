import pygame


class Hole:

    def __init__(self, x: int, y: int, color: tuple, radius: int):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
