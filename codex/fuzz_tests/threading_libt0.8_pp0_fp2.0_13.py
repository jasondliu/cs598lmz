import threading
threading.stack_size(2**27)
import sys
import pygame
import pickle

#Initialize the pygame module
pygame.init()
#Load and set the logo
pygame.display.set_caption("minimal program")
#Set a background image
#background_image = pygame.image.load("saturn_family1.jpg").convert()
#background_image = pygame.transform.scale(background_image, (1300,800))
#Define a surface to draw on
global screen, gameState
gameState = GameState()
system = ClientSystem(gameState)

size = width, height =1000, 600
screenSize = width/2, height/2
screen = pygame.display.set_mode(size)

def runGame():
    # font = pygame.font.Font(None, 32)
    # text = font.render("Hello There", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = screen.get_rect().centerx
    screen.fill(
