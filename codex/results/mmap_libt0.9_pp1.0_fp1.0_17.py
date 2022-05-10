import mmap
import numpy as np
from collections import deque
import pyaudio
import time
import threading
import Queue

# -------------------------------------           
#             CONSTANTS
# -------------------------------------

BAR_LEN = 32          # num of pixels per line
WIDTH = BAR_LEN * 15  # width of the screen.
HEIGHT = 64  # height of the screen.
FPS = 40
BARS = 150
#k = 3                  # gain for weighted averaging
bias = 20
thresh = 45
inc = 1.0             # how much to increment increment by
inc_dec = 0.005       # how fast to decrease increments.
PENWIDTH = 2 # how many pixels wide is the line
#SPEED = 0.1            # 0.0-1.0 speed of the bars when decay is on

DRUMS = 0
BASS = 1
MUSIC = 2

LOW_BASS = 0
MID_BASS = 1
HIGH_BASS = 2

DRUMAVERAGELEVEL = 0.5
BASSAVERAGELE
