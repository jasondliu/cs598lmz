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

print("creating globals")
globals().update(vars(latefin.ref()))
del latefin

print("creating C frame")
# initialize C frame
import sys
sys.settrace(lambda *x: None)

print("creating long stack")
# create a long stack
def f():
    return f()
try:
    f()
except RecursionError:
    pass

print("testing: ", end='')
try:
    func()
except ReferenceError:
    print("OK")
else:
    print("failed!")
