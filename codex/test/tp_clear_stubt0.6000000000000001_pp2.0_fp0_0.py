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

# The above code creates a finalizer that holds a weak reference to the
# function, and also a reference to the finalizer from the function.  The
# finalizer is run after the function is destroyed, and sets the global
# variable "func" to the weak reference.  The weak reference is cleared
# when the function is destroyed, but the finalizer is still run.  After
# the finalizer is run, the weakref is still alive, but points to a dead
# function.  Calling the weak reference will then raise a
# ReferenceError.

try:
    f = func()
except ReferenceError:
    print("ReferenceError")

try:
    func()
except ReferenceError:
    print("ReferenceError")

try:
    latefin.ref()
except ReferenceError:
    print("ReferenceError")
