import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect can be called after all constructor
# references have gone out of scope
# Note that all possible circular references through
# supported.__module__ must be eliminated.
class supported(object):
    def __new__(cls):
        return object.__new__(cls)
    def __init__(self):
        self.__module__ = weakref.ref(self)
    def __del__(self):
        self.ok = True
s = supported()
w = weakref.ref(s)
gc.collect()
assert s.ok is True
# Test gc.collect can be called after all constructor and
# destructor references have gone out of scope.
# Note that all possible circular references through
# destructor.__module__ must be eliminated.
class destructor(object):
    def __new__(cls):
        return object.__new__(cls)
    def __init__(self):
        self.ok = False
        self.__module__ = weakref.ref(self)
    def __del__(self):
        self.__module__ = None
s
