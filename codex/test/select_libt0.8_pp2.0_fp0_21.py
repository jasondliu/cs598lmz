import select
import time
import math

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


class Escape:
    def __init__(self):
        self.FPS = 30
        self.WIDTH = 1024
        self.HEIGHT = 768
        self.MUSIC_END = pygame.USEREVENT+1
        self.playing = False
        self.image = pygame.image.load("./screenshot.bmp")
        self.image = pygame.transform.scale(self.image, (self.WIDTH*3, self.HEIGHT*3))
        self.image = self.image.convert_alpha()
        self.pos = [0, 0]
        self.speed = [1,1]
        self.screensize = [self.WIDTH, self.HEIGHT]
        self.screen = pygame.display.set_mode(self.screensize)
        pygame.display
