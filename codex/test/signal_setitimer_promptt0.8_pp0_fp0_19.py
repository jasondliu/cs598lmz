import signal
# Test signal.setitimer before using it
try:
    signal.setitimer(signal.ITIMER_REAL, 1)
except:
    def signal_handler(signum, frame):
        pass
    signal.signal(signal.SIGALRM, signal_handler)

import sys
import copy

from pyglet import clock, image, window
from pyglet.gl import *

import graphics, interface
from config import *
import display, graphics, interface, statemachine, timeline, create
import master
from master import FPS, RESOLUTION, TILESIZE, STATUS_BAR, FOV_LIGHT_WALLS
import log
import server
import util
import items
import magic
import player
import monster
import effects
import colours
import savegame
import status
import ruletable
import turn
import npc
import skills
import races
import classes
import feats
import spells
import enchantments
import sound
import common
import mouse

SIZE = RESOLUTION[0]-32, RESOLUTION[1]-STATUS_BAR-32

#-----------------------------------------------------------------------------


