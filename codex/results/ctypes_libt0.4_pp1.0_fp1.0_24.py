import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame
from pygame.locals import *

from classes.game import Game
from classes.player import Player
from classes.enemy import Enemy
from classes.bullet import Bullet
from classes.explosion import Explosion
from classes.powerup import Powerup
from classes.text import Text

from constants import *
from functions import *

pygame.init()
pygame.mixer.init()

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Asteroids')

# Initialize game clock
clock = pygame.time.Clock()

# Initialize game objects
game = Game()
player = Player()

# Initialize lists for game objects
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()
powerups = pygame.sprite.Group()
