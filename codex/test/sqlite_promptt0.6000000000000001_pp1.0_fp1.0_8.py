import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import os
import sys
import traceback
import time
import copy
import logging
import logging.config
import logging.handlers
import socket
import struct
logger = logging.getLogger(__name__)

import rtmidi
from rtmidi.midiutil import open_midiport
import mido

from . import midi
from . import midi_message
from . import config

import app.util

class MidiIO(object):

    def __init__(self, input_port_name=None, output_port_name=None):
        self.input_port_name = input_port_name
        self.output_port_name = output_port_name
        self.input_port = None
        self.output_port = None
        self.input_port_open = False
        self.output_port_open = False

