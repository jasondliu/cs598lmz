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
general_midi_instrument_names = [
    "grand piano",
    "bright piano",
    "electric grand",
    "honky-tonk piano",
    "electric piano 1",
    "electric piano 2",
    "harpsichord",
    "clavi",
    "celesta",
    "glockenspiel",
    "music box",
    "vibraphone",
    "marimba",
    "xylophone",
    "tubular bells",
    "dulcimer",
    "drawbar organ",
    "percussive organ",
    "rock organ",
    "church organ",
    "reed organ",
    "accordion",
    "harmonica",
    "tango accordion",
