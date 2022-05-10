import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
from time import time
from random import randint
from math import floor
import numpy as np
from numpy.random import randint as rand

#Global variables
#width and height of the screen
w = 600
h = 600
#number of rows and columns of the board
n = 20
#size of each cell
size = int(w/n)
#number of mines
m = 100
#initialize pygame
pygame.init()
#initialize the screen
screen = pygame.display.set_mode((w, h))
#initialize the font
font = pygame.font.SysFont("comicsansms", 20)
#set the caption of the window
pygame.display.set_caption("Minesweeper")
#set the icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
#initialize the clock
clock = pygame.time.Clock()
#initialize the running variable
running
