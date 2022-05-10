import ctypes
# Test ctypes.CFUNCTYPE()

__version__ = "2.0"
__author__ = "Miki Tebeka <miki.tebeka@gmail.com>"

Interval = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def interval(low, high):
    """Return a random number between low and high"""
    return random.randint(low, high)

i = Interval(interval)
print "Random number between 10 and 20 =", i(10, 20)
print "Random number between 1 and 10 =", i(1, 10)
