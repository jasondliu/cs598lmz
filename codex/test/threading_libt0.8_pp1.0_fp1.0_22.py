import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
FPS = 30
fpsClock = pygame.time.Clock()
font = pygame.font.Font(None, 20)
speed = 0
x,y = 0,0
x1,y1 = 0,0
x2,y2 = 0,0
x3,y3 = 0,0
x4,y4 = 0,0
x5,y5 = 0,0
plpos = (400,300)
sm1pos = (x,y)
sm2pos = (x1,y1)
sm3pos = (x2,y2)
sm4pos = (x3,y3)
sm5pos = (x4,y4)
sm6pos = (x5,y5)

