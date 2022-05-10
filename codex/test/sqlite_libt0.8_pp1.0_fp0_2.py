import ctypes
import ctypes.util
import threading
import sqlite3

import pygame
import pygame.midi

import config as cfg
from controller import Controller
from states import OffState, OnState, AutoOnState

event_buffer_size = 128
max_midi = 128

# http://www.midi.org/techspecs/gm1sound.php
