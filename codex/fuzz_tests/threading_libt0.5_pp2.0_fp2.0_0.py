import threading
threading.stack_size(2**27)
import sys
import math
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import random
import os
import argparse
import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
import torchvision.transforms as T
from PIL import Image

# Initialize the game
pygame.init()
pygame.display.set_caption("Simulated Environment")
screen = pygame.display.set_mode((600, 600), 0, 32)
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0.0, -900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Define the parameters
TIME_
