import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import logging
logging.basicConfig(level=logging.DEBUG)

import sys
import os
import os.path
import time

import unittest

from . import common

from . import ffi
from . import rtmidi

class TestMidiOut(common.MidiOutTestCase):
    def test_open_port(self):
        self.midiout.open_port(0)
        self.midiout.close_port()

    def test_open_virtual_port(self):
        self.midiout.open_virtual_port("test_open_virtual_port")
        self.midiout.close_port()

    def test_send_message(self):
        self.midiout.open_virtual_port("test_send_message")
        self.midiout.send_message([0x80, 60, 100])
        self.midiout.close_port()

