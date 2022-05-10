import weakref
# Test weakref.ref
import gc

class C:
    def __init__(self, a):
        self.a = a
