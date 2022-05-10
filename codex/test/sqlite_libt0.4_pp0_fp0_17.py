import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import time
import math

# Create the libspotify object
libsp = ctypes.CDLL(ctypes.util.find_library('spotify'))

# Create the spotify object
spotify = ctypes.c_void_p()

# Create the config object
config = ctypes.c_void_p()

# Create the session object
session = ctypes.c_void_p()

# Create the connection object
connection = ctypes.c_void_p()

# Create the audio object
audio = ctypes.c_void_p()

# Create the track object
track = ctypes.c_void_p()

# Create the track object
track_playing = ctypes.c_void_p()

# Create the playlist object
playlist = ctypes.c_void_p()

# Create the playlist container object
playlistcontainer = ctypes.c_void_p()

# Create the search object
search = ctypes.c_void_p()

# Create the artist object
