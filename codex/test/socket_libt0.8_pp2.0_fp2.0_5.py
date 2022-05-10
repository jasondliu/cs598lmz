import socket
import threading
import time
import collections
import Queue

from kite import Kite

# A "global" clock for tracking experiment time
class Clock(object):
    def __init__(self, start_time=0):
        self._t = start_time
        self._offset = 0
        self._locks = []
    @property
    def time(self):
        return self._t
    def reset(self, start_time=0, offset=0):
        self._t = start_time
        self._offset = offset
    def update(self, t):
        self._t = t
    def advance(self, dt):
        self._t += dt
        return self._t
    def __iadd__(self, dt):
        self._t += dt

