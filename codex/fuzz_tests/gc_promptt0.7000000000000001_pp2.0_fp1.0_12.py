import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()
gc.collect()
# Test gc.is_tracked()
class A:
    def __init__(self):
        self.__priv = 42
    def getpriv(self):
        return self.__priv
    def setpriv(self, value):
        self.__priv = value
    def delpriv(self):
        del self.__priv
    priv = property(getpriv, setpriv, delpriv)
a = A()
a.priv
a.priv = 1
a.priv
del a
# Test gc.get_objects()
# Test gc.get_referrers()
# Test gc.get_referents()
# Test gc.get_threshold()
# Test gc.set_threshold()
# Test gc.DEBUG_STATS
# Test gc.DEBUG_LEAK
# Test gc.DEBUG_COLLECTABLE
# Test gc.DEBUG_UNCOLLECTABLE
# Test gc.DEBUG_INSTANCES
# Test gc.DEBUG_OBJECTS
