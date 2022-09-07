# coding:utf-8


"""
TODO:
	> make arrow [x]
	> make blocks [x]
	> make power bar [x]
	> make label score (nb of shot) []
	> make levels logic []

Basic golf game made with pygame,
by: ma0
"""

import pygame
import random

from modules.ball import Ball
from modules.hole import Hole
from modules.arrow import Arrow
from modules.block import Block
from modules.score import Score



pygame.init()

# game constants
TITLE = 'GOLF'
WIDTH = 700
HEIGHT = 1000
BACKGROUND_COLOR = (0, 255, 0)
FPS = 60

# ball constants
BALL_COLOR = (255, 255, 255)
BALL_RADIUS = 20

# hole constants
HOLE_COLOR = (0, 0, 0)
HOLE_RADIUS = (15)

# screen parameters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# variables
running = True

# functions

def reset():
	hole.__init__(random.randint(10, WIDTH), random.randint(10, HEIGHT), HOLE_COLOR, HOLE_RADIUS)
	ball.__init__(random.randint(10, WIDTH), random.randint(10, HEIGHT), BALL_COLOR, BALL_RADIUS)
	score.__init__(10, 10, 10, 10)

def update():

	hole.draw(screen)
	score.draw(screen)
	block.draw(screen)
	ball.update(screen, WIDTH, HEIGHT, hole, block)

	if ball.reset is True:
		reset()

	pygame.display.flip()
	screen.fill(BACKGROUND_COLOR)


# objects
clock = pygame.time.Clock()
ball = Ball(150, 150, BALL_COLOR, BALL_RADIUS)
hole = Hole(random.randint(10, WIDTH), random.randint(10, HEIGHT), HOLE_COLOR, HOLE_RADIUS)
block = Block(300, 350, 100, 500, (0, 0, 255))
score = Score(10, 10, 10, 10)

# ------------------------ main loop -------------------------------
while running:

	# --------------------- EVENTS -----------------------------------------
	for events in pygame.event.get():

		# quit game
		if events.type == pygame.QUIT:
			running = False

		if events.type == pygame.MOUSEBUTTONDOWN:
			coord1 = (ball.x, ball.y)
			ball.aiming = True

		if events.type == pygame.MOUSEBUTTONUP:
			coord2 = pygame.mouse.get_pos()
			ball.shot(coord1, coord2, score)

		if events.type == pygame.KEYDOWN:
			if events.key == pygame.K_SPACE:
				reset()


	# -------------------------------------------------------------------

	update()
	clock.tick(FPS)
# ----------------------- end main loop ---------------------------------
pygame.quit()
