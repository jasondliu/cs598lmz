import ctypes
# Test ctypes.CFUNCTYPE()

__version__ = "2.0"
__author__ = "Miki Tebeka <miki.tebeka@gmail.com>"

Interval = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def interval(low, high):
    """Return a random number between low and high"""
    return random.randint(low, high)

i = Interval(interval)
