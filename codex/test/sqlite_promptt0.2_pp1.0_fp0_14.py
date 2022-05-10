import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# This is a simple example of how to use the libspotify API to log in and
# play a track.

# The example app key must be replaced with a valid one, which is available
# when you have a Spotify Premium account.

# This example uses the simple callback dispatcher, which is a single-threaded
# dispatcher that makes it easy to use libspotify from a single-threaded
# environment. See the thread_example.py for how to use the main loop
# dispatcher, which is a bit more complex but which can also be used from
# multi-threaded programs.

# Documentation about the libspotify API can be found at:
# https://developer.spotify.com/technologies/libspotify/docs/12.1.51/

import sys
import spotify
import time
import threading
import Queue

import spotify

session = spotify.Session()

# Process events in the main thread
