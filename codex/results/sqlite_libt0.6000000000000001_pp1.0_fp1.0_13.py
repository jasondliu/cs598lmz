import ctypes
import ctypes.util
import threading
import sqlite3
import logging
import os

import pygame
import pygame.midi

from . import config

logger = logging.getLogger(__name__)

# alsa and portmidi require threading
if pygame.midi.get_init():
    pygame.midi.quit()
pygame.midi.init()

# System MIDI input device
MIDI_SYSTEM_INPUT = pygame.midi.get_default_input_id()

# System MIDI output device
MIDI_SYSTEM_OUTPUT = pygame.midi.get_default_output_id()

# Device ID for keyboard
MIDI_KEYBOARD = -1

# Device ID for virtual MIDI output port
MIDI_VIRTUAL_OUTPUT = -2

# Device ID for virtual MIDI input port
MIDI_VIRTUAL_INPUT = -3

# Device ID for virtual MIDI input/output port
MIDI_VIRTUAL_IO = -4

# This is a virtual device, used to connect to a running instance
