import threading
threading.stack_size(2**27)
import sys
import glob
import errno
import pickle
import os
import math
import time
import pyaudio
import wave
from datetime import datetime


def find_files(directory):
    paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            paths.append(filepath)
    return [path for path in paths if path.endswith('.wav')]


def read_wave(path):
    with contextlib.closing(wave.open(path, 'rb')) as wf:
        channels = wf.getnchannels()
        rate = wf.getframerate()
        frames = wf.getnframes()
        buffer = wf.readframes(frames)
        return buffer, rate, channels


