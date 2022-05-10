import ctypes
import ctypes.util
import threading
import sqlite3
import pygame
import random
import time
import sys
import os
import itertools
import subprocess
import json
import pyaudio
import wave

def rt_sort(a,b):
    return a[0]-b[0]

def rt_sort_c(a,b):
    return a[1]-b[1]

def chunk(audio,chunk_size):
    while 1:
        data = audio.read(chunk_size)
        if data:
            yield data
        else:
            break

def rec(filename,audio,stream,chunk_size,sample_rate,duration,channels):
    frames = []
    while len(frames)/(sample_rate*1.0) < duration:
        data = stream.read(chunk_size)
        frames.append(data)
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
