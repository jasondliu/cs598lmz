import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

# Test for python 2.6
_random = random.SystemRandom()

class _UnavailableRNG(object):
    def random(self):
        raise NotImplemented("System default random number generator not available")
    def seed(self, seed):
        raise NotImplemented("System default random number generator not available")

try:
    _rng = random.SystemRandom()
except:
    _rng = _UnavailableRNG()

# Some platforms don't have a random number generator
random.randint = _rng.randint
random.seed = _rng.seed

try:
    long(1)
except NameError:
    long = int

# Python2 compatibility
try:
    xrange(0)
except NameError:
    xrange = range

def _bytes(x):
    try:
        return x.encode("utf-8")
    except AttributeError:
        return x

