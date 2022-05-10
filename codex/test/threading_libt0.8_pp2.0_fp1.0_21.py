import threading
threading.stack_size(2**27)
import sys
import pygame
from pygame.locals import *
import os
import random
import math
import Tkinter
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import json

#constants
PI = 3.141592653

pygame.init()

#fonts
font_scoreA = pygame.font.SysFont("Arial", 30)
font_scoreB = pygame.font.SysFont("Arial", 30)
font_bestscore = pygame.font.SysFont("Arial", 20)
font_loseA = pygame.font.SysFont("Arial", 100)
font_loseB = pygame.font.SysFont("Arial", 100)
font_winA = pygame.font.SysFont("Arial", 100)
font_winB = pygame.font.SysFont("Arial", 100)
font_wel = pygame.font.SysFont("Arial", 40)
font_inst = pygame.font.SysFont
