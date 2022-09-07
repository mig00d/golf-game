import pygame
import math
import time

from modules.arrow import Arrow

class Ball:
    def __init__(self, x: int, y: int, color: tuple, radius: int):

        # ball seting
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

        # ball movement seting
        self.speed = 0
        self.deccel = 0.2
        self.dirx = 0
        self.diry = 0
        self.pow = 0
        self.max_pow = 30

        # logic bool
        self.shooted = False
        self.falling = False
        self.reset = False
        self.aiming = False

    def draw_arrow(self, surface):
        """ draw the directionnal arrow of the shot """

        mouse_pos = pygame.mouse.get_pos()

        arrow = Arrow(self.x, self.y, (255, 0, 0), 15)
        arrow_vec = get_vector((arrow.x, arrow.y), pygame.mouse.get_pos())
        arrow_direction = normalize_vector(arrow_vec)

        arrow_length = get_vector_length(arrow_vec) // 2
        arrow.draw(surface, arrow_direction, arrow_length)


    def reset_shot(self):
        """ Reset one shot for the prox """
        self.pow = 0
        self.speed = 0
        self.shooted = False


    def move(self):

        if self.speed > 0:
            self.speed -= self.deccel
            self.x += self.speed * self.dirx
            self.y += self.speed * self.diry
            self.pow -= 10


    def shot(self, coord1: tuple, coord2: tuple, shot_counter):
        """ Shot in the ball """

        self.aiming = False

        vector = get_vector(coord1, coord2)
        shot_direction = normalize_vector(vector)

        if not shot_direction[0] == 0 and not shot_direction[1] == 0:
            self.dirx = shot_direction[0]
            self.diry = shot_direction[1]

        self.pow = 0
        self.pow = min(get_vector_length(vector) // 10, self.max_pow)

        self.speed = self.pow

        shot_counter.add_score()


    def falling_animation(self):
            self.speed = 0
            self.current_speed = 0
            self.pow = 0

            while self.radius > 0:
                self.radius -= 0.5


    def check_collision(self, screen_width: int, screen_height: int, hole, block):
        """ Check all collisions with the player """

        # --------- WINDOW BORDER COLLISION ---------------
        if self.x > screen_width or self.x < 0:
            self.dirx *= -1
        if self.y > screen_height or self.y < 0:
            self.diry *= -1
        # -------------------------------------------------

        # --------- HOLE COLLISION -------------------------
        if math.sqrt((self.x - hole.x) ** 2) < self.radius and math.sqrt((self.y - hole.y) ** 2) < 30:
            self.falling_animation()
            self.reset = True

        # -------------------------------------------------

        # --------- BLOCK COLLISION ----------------------

        if self.y > block.y and self.y < block.y + block.height and self.x > block.x and self.x < block.x + block.width:
            self.dirx *= -1

        if self.x > block.x and self.x < block.x + block.width and self.y > block.y and self.y < block.y + block.height:
            self.diry *= -1


    # ---------------- UPDATE --------------------------------------
    def update(self, surface, screen_width: int, screen_height: int, hole, block):
        """ Functions call per frame """

        self.check_collision(screen_width, screen_height, hole, block)

        self.move()

        self.draw(surface)


    def draw(self, surface):
        """ Draw the ball end all the sprites wich is asociated to the ball """
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

        if self.aiming is True:
            self.draw_arrow(surface)

# --------------- statics methods ----------------------------------------

def get_vector(A: tuple, B: tuple) -> tuple:
    return (B[0] - A[0], B[1] - A[1])


def get_shot_pow(A: tuple, B: tuple) -> int:
    """ Get the shot power (distance between the coords)"""
    return (B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2


def normalize_vector(vector: tuple) -> tuple:
    """ Get the shot direction (normalize)"""

    vector_length = get_vector_length(vector)

    try:
        return -(vector[0] / vector_length), -(vector[1] / vector_length)
    except ZeroDivisionError:
        return (0, 0)


def get_vector_length(vector: tuple) -> float:
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)
