import threading
threading.stack_size(2**27)
import sys
import ctypes
ctypes.cdll.LoadLibrary('libSDL2.so')
import pygame
import random
import math
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Pygame Platformer')
    clock = pygame.time.Clock()
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite
