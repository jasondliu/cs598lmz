import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
import pygame
import random
import math
import pygame.gfxdraw

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Shooter")

bullet = None

bg = pygame.image.load('images/bg.png')

class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.health = 100
        self.img = img2 = pygame.image.load('images/player.png')
        if bullet == None:
            self.weapon = None
        self.left = False
        self.right = False
        self.mdown = False

    def draw(self, win):
        if self.left == True:
            self.img = pygame.image.load('images/player2.png')
