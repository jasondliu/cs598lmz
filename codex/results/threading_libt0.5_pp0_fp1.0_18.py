import threading
threading.stack_size(2**27)

# Importing libraries
import pygame
from pygame.locals import *
import random
import time
import sys
import os

# Importing classes
from Snake import Snake
from Food import Food
from Game import Game

# Initializing Pygame
pygame.init()

# Setting up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

# Loading images
background = pygame.image.load('Images/background.png')

# Creating the snake
snake = Snake()

# Creating the food
food = Food()

# Creating the game
game = Game()

# Creating the main loop
while True:
    # Setting the fps
    clock = pygame.time.Clock()
    clock.tick(30)

    # Drawing the background
    screen.blit(background, (0, 0))

    # Drawing the snake
    snake.draw(screen)

    # Drawing the food
    food.draw(screen)

    # Drawing the score
