import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
from model import *

paddleH = 10
paddleW = 75
paddleMargin = 10
ballSize = 10

black = 0, 0, 0
white = 255, 255, 255

# Initialize model
model = Model()

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption('Pong')

# Initialize clock
clock = pygame.time.Clock()

# Initialize screen
screen.fill(black)

# Initialize paddles
paddleA = pygame.Rect(paddleMargin, (450 - paddleH) / 2, paddleW, paddleH)
paddleB = pygame.Rect(600 - paddleW - paddleMargin, (450 - paddleH) / 2, paddleW, paddleH)

# Initialize ball
ball = pygame.Rect(300, 225, ballSize, ballSize)

# Initialize
