import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()
del(latefin)

# The bug is that the module refcount was incorrectly decremented in
# slot_tp_dealloc() by a call to incref while holding the thread state (so
# decref will be happy to unlock the GIL even though we still hold a ref).
# Calling the dealloc function makes the assertion fail, i.e. the module
# refcount reaches a negative value.
func = ''
