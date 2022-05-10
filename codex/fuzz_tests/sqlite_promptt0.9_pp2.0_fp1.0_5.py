import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# conn = sqlite3.connect('data/database.ssdb')
# print(conn.execute('select * from sqlite_master').fetchall())

# Python-Aubio must be installed before running this program
aubiowrapper = aubio
import wave
import sys
import getopt
import os

# Global variables for wave file and processing
CHANNELS = 1
SAMPLEWIDTH = 2
FRAMERATE = 44100
NFRAMES = 2048

total_num_frames = 0


def processFile(inputFile, window, hop_size, samplerate):
    print("Processing file: " + inputFile)

    # sourceFile = wave.open(inputFile, 'rb')
    # sourceFile.seek(44)  # 44 is the header
    #
    # outputFile = wave.open(inputFile.replace('.wav', '-ss.wav'), 'wb')
    # outputFile.setparams((CHANNELS, SAMPLEWIDTH, FRAMERATE, NFRAMES, 'NONE', 'not compressed'))

