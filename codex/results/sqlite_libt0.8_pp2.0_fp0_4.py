import ctypes
import ctypes.util
import threading
import sqlite3 as lite
import datetime

import dbus.service

import sys
sys.path.append('./') # make sure the libs can be found

import lib

class BaseWatcher(object):
    def __init__(self,serial=None):
        self.serial = serial

class AudioWatcher(BaseWatcher):
    def __init__(self, serial=None):
        super(AudioWatcher, self).__init__(serial)

        self.buffer_size=1024
        self.sample_rate = 44100
        self.pa = pyaudio.PyAudio()

    def session_callback(self, in_data, frame_count, time_info, status):
        print in_data
        return (None, pyaudio.paContinue)

    def start(self):
        self.stream = self.pa.open(format=pyaudio.paInt16,
                           channels=2,
                           rate=self.sample_rate,
                           input=True,
                           frames_per_buffer=self.buffer_size,
                           stream_
