import ctypes
import ctypes.util
import threading
import sqlite3
import time
import random

# This is a modified version of the original
# https://github.com/sashahilton00/chirp-python/blob/master/chirp/chirp.py

# This is the callback function that will be passed to the Chirp library to be
# called when a Chirp is received.
def receive_callback(payload, length, channel):
    print('Received Chirp: %s' % (payload[:length]))

# This is the callback function that will be passed to the Chirp library to be
# called when a Chirp is sent.
def sent_callback(payload, length, channel):
    print('Sent Chirp: %s' % (payload[:length]))

# This is the callback function that will be passed to the Chirp library to be
# called when the state of the Chirp library changes.
def state_callback(state):
    print('State changed: %s' % state)

# This is the callback function that will be passed to the Chirp library
