import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H"),daemon=True).start()

import pygame
from pygame.locals import *
pygame.init()

def draw(pos, col):
    pygame.draw.circle(screen, col, pos, 6)

screen = pygame.display.set_mode((500,500))

def init(size):
    global grid, nextc, nextr
    grid = [[(0,0,0) for i in range(size)] for i in range(size)]
    nextc, nextr = 0, size - 1

def txt(pos, txt):
    font = pygame.font.Font(None, 20)
    text = font.render(txt, 1, (255,255,255))
    textpos = text.get_rect()
    screen.blit(text, (pos[0]+5,pos[1]-5))

def draw_grid(size):
    for row in range(size):
        for col in range(size):
            t
