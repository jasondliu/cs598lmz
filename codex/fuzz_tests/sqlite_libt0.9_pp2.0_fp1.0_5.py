import ctypes
import ctypes.util
import threading
import sqlite3
from sys import platform as _platform

mac_speaker = ctypes.util.find_library('speaker')
speaker = ctypes.cdll.LoadLibrary(mac_speaker)

if _platform == "linux" or _platform == "linux2":
# linux
    speaker = ctypes.CDLL('libspeaker.so')
elif _platform == "darwin":
# MAC OS X
    speaker = ctypes.CDLL('libspeaker.dylib')
elif _platform == "win32":
# Windows
    speaker = None
    
# Define output frequencies
SPEAKER_BEEP_ONCE = 1
SPEAKER_BEEP_TWICE = 2
SPEAKER_BEEP_TRIPLE = 3
SPEAKER_BEEP_FOUR = 4
SPEAKER_BEEP_FIVE = 5
SPEAKER_BEEP_SIX = 6
SPEAKER_BEEP_SEVEN = 7
SPEAKER_BEEP_EIGHT = 8
SPEAKER_BEEP_NINE =
