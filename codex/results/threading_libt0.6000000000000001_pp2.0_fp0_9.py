import threading
threading.stack_size(67108864)

def run_game(x,y,z):
    try:
        import pygame
        import sys
        import random
        import os
        import time
        import copy
        import math
        import operator
        import glob
        import random
        import pickle
        import datetime
        import pygame.locals as GAME_GLOBALS
        import pygame.event as GAME_EVENTS
        import pygame.time as GAME_TIME
        import pygame.font as GAME_FONT
        import pygame.image as GAME_IMAGE
        import pygame.mixer as GAME_MIXER
        import pygame.mouse as GAME_MOUSE
        import pygame.draw as GAME_DRAW
        import pygame.display as GAME_DISPLAY
        import numpy as np

        from pygame.locals import (
            RLEACCEL,
            K_UP,
            K_DOWN,
            K_LEFT,
            K_RIGHT,
            K_ESCAPE,
            KEYDOWN,
           
