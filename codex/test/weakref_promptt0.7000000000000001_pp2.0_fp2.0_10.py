import weakref
# Test weakref.ref for objects which (1) can be weakly referenced, and (2)
# have a __del__ method which raises an exception when called.  The
# reference must become invalid when the referent is deleted.

class C:
    def __init__(self, callback):
        self.callback = callback
    def __del__(self):
        self.callback(self)
        raise ValueError

