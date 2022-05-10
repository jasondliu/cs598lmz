import select
import socket

import colorsys
import random
import pyaudio
import threading
import traceback
import sys

HOST = "127.0.0.1"
PORT = 8888

CHUNK = 1024 * 16
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

MAX_AMPLITUDE = 32768.0

class color_thread(threading.Thread):
    def __init__(self, bar_index, bar_length, color, streaming, also_stdout):
        threading.Thread.__init__(self)

        self.bar_index = bar_index
        self.bar_length = bar_length
        self.color = color
        self.streaming = streaming
        self.also_stdout = also_stdout

    def run(self):
        try:
            self.run2()
        except:
            traceback.print_exc()
            sys.exit(1)

