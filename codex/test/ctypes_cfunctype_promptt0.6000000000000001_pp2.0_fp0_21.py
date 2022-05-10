import ctypes
# Test ctypes.CFUNCTYPE

class X(object):
    def __init__(self, x=0):
        self.x = x

def callback(x):
    x.x = 1

