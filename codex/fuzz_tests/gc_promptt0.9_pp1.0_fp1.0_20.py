import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when the tp_traverse slot is NULL
class myclass:
    pass

a = myclass()
b = myclass()
print(gc.collect())

# test attribute admin when tp_traverse slot is NULL
a.__dict__ = None
b.__dict__ = None
del a, b

gc.collect()
# Test gc.collect() when a strong reference is not scan
class myclass:
    def __traverse__(self, visitor):
        return
    def __del__(self):
        pass

a = myclass()
g = a.__dict__
a.__dict__ = None
del a, g
gc.collect()
