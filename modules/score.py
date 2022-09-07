import pygame


class Score:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = 0

    def add_score(self):
        self.score += 1

    def draw(self, surface):
        print(self.score)
