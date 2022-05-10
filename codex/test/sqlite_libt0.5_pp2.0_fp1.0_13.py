import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import traceback
import datetime
import platform
import re

import pygame.midi
import pygame.mixer

import midi
import midi.sequencer

import config
import util

import logging
log = logging.getLogger()

class Player(object):
    def __init__(self, sequencer):
        self.sequencer = sequencer
        self.sequencer.register_callback(self.sequencer_callback)
        self.event_queue = []
        self.event_queue_lock = threading.Lock()
        self.playing = False
        self.paused = False
        self.song_id = None
        self.song_name = None
        self.song_artist = None
        self.song_album = None
        self.song_length = 0
        self.song_position = 0
        self.song_position_lock = threading.Lock()
        self.song_volume = 0
        self.song_volume_lock = threading.Lock()
        self.song_tem
