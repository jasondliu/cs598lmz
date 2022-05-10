import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
from src.game import Game

def main():
    pygame.init()
    pygame.display.set_caption("The Mummy")
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
