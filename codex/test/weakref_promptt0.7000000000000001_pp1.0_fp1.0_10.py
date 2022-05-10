import weakref
# Test weakref.ref() for objects with a destructor.
import gc
import sys

class C:
    def __init__(self):
        self.x = 1
