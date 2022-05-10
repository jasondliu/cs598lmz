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
</code>
What I need to do is find out why this code raises a Segmentation Fault.
The Python 3.2 documentation says that this version uses a cycle detection algorithm to prevent infinite recursion when deallocating cycles like this one, but I can't understand it.


A:

This is a bug in Python's garbage collection (which is already fixed in Python 3.2 HEAD). 
The problem is that the methods in the weakref module do not tell the garbage collector that the underlying <code>Cyclic</code> cycle is still alive. Even though the <code>func</code> reference cycle is alive, the <code>LateFin</code> object (the <code>func()</code> return value) is not kept alive, because of the above-mentioned problem.

