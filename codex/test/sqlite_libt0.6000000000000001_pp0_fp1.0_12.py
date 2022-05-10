import ctypes
import ctypes.util
import threading
import sqlite3
import time
import pyaudio
import wave
import uuid
import os
import subprocess
import json


class SoundProc(threading.Thread):
    """
    This class is the sound processing class. It is used to record sound and save it to
    a file.
    """
    def __init__(self, stream, CHUNK, FORMAT):
        """
        The constructor for the sound processing class
        :param stream: the stream to record from
        :param CHUNK: the chunk size of the stream
        :param FORMAT: the format of the stream
        """
        threading.Thread.__init__(self)
        self.stream = stream
        self.CHUNK = CHUNK
        self.FORMAT = FORMAT

    def run(self):
        """
        This method is called when the thread is started. It records sound from the stream and
        saves it to a file.
        :return: None
        """
        start_time = time.time()
        frames = []
        while time.time() - start_time < 3:
            frames
