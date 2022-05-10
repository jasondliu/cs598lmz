import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

#%%
# import pygame
import random
import numpy as np
import time
import matplotlib.pyplot as plt
import math
import cv2
import os

#%%
# Initialize the game
pygame.init()

#%%
# Display the game
pygame.display.set_caption("T-Rex Rush")
screen = pygame.display.set_mode((600,150))

#%%
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)

#%%
# Load the sprites used in the game
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'sprites') # The resource folder path

#%%
# Load the images
