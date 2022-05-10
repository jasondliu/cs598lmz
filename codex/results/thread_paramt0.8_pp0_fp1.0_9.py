import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[r'), daemon=True).start()

import pygame
from pygame.locals import *
import os
import random

class Game:
    def __init__(self, width, height):
        self.song_name = get_song_name()
        self.score = 0
        self.width = width
        self.height = height
        self.FPS = 30
        self.pause = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Music Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        
        self.bg_image = pygame.image.load(os.path.join('graphics', 'background.jpg')).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (width, height))

        self.notes
