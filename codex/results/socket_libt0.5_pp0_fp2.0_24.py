import socket
import sys
import threading
import time

import pygame
from pygame.locals import *

from network import Network
from player import Player

pygame.init()
pygame.font.init()

pygame.display.set_caption('SNAKE')

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans MS', 30)

bg = pygame.image.load('images/bg.png')

class Game:
    def __init__(self, ip, port, n):
        self.n = n
        self.network = Network(ip, port)
        self.player = self.network.getP()

    def run(self):
        run = True
        while run:
            clock.tick(60)
            self.player.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    sys
