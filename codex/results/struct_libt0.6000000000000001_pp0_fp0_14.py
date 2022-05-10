import _struct
import string
import time
import cPickle as pickle
import pygame
import math
import random
import sys
import os

class Timer:
    def __init__(self, t_limit):
        self.limit = t_limit
        self.time = 0
    def tick(self):
        self.time += 1
        if self.time >= self.limit:
            self.time = 0
            return True
        return False

class Map:
    def __init__(self, map_file):
        self.map = []
        self.tile_size = 0
        self.load_map(map_file)
    def load_map(self, map_file):
        file = open(map_file, "r")
        self.tile_size = int(file.readline())
        for line in file:
            line = line.strip()
            self.map.append(line)
        file.close()

class Player:
    def __init__(self, game):
        self.x = 0
        self.y = 0
       
