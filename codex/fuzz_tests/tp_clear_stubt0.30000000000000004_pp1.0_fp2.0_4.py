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

# This is the interesting part:
# The weakref callback is invoked, and the LateFin object is destroyed.
# The LateFin object's __del__ method tries to set the func variable.
# The func variable is a local variable in the scope of the function.
# The function is a closure, and its closure cell is in the Cyclic object.
# The Cyclic object is in the process of being destroyed, and the
# func variable is in the process of being deleted.
# The func variable is a local variable in the scope of the function,
# and the function is a closure, and the closure cell is in the Cyclic
# object, which is in the process of being destroyed, and the func
# variable is in the process of being deleted.
# The func variable is a local variable in the scope of the function,
# and the function is a closure, and the closure cell is in the Cyclic
# object, which is in the process of being destroyed, and the func
# variable is in the process of being deleted.
# The func variable is a local variable in the scope of the function,
# and the
