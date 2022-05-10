import threading
threading.stack_size(2**27)
import sys
import pygame
import random
import math

# import from the 21 Bitcoin Developer Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

# import from the 22 Blockgeeks Library
from blockchain import blockexplorer

# import from the Python Imaging Library
from PIL import Image

# import io for capturing bytes
import io

# Server-side configuration
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

# Configure PyGame and key bindings
pygame.init()
pygame.display.set_caption("Bitcoin Block Explorer")
screen = pygame.display.set_mode((1024, 768))
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

# Constants
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED
