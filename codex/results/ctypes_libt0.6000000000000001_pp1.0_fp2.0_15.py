import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Pong Game")

# import libraries
import pygame
import math
import random


# create the game window
pygame.init()
WIDTH,HEIGHT = 600,600
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong Game")

# load the images
ball = pygame.image.load('ball.png')
paddle_1 = pygame.image.load('paddle_1.png')
paddle_2 = pygame.image.load('paddle_2.png')

# font
font = pygame.font.Font('freesansbold.ttf',32)

# ball initial position
ball_x = WIDTH//2-30
ball_y = HEIGHT//2-30
ball_change_x = 0
ball_change_y = 0

# paddle initial position
paddle_1_x = 10
paddle_1_y = HEIGHT//2-50
paddle_1_change_y
