import pygame


class Arrow:
    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, surface, vec, length):

        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.line(surface, self.color, (self.x, self.y),

        (self.x + length * vec[0] , self.y + length * vec[1]), width= self.width)
