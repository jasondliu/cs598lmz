import weakref
# Test weakref.ref() with a class that overrides __del__.
# This was broken in Python 2.2.1.

class C(object):
    def __init__(self, name):
        self.name = name
