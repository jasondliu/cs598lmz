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
if latefin.ref is None:
    print("ok")
</code>
I'm using the by-name closure to prevent the <code>func</code> object being held by the cyclic reference. Unfortunately, when trying to reduce this, the slice of <code>func</code> in <code>_PyCode_Consts</code> appears to hold a reference to the object.
Can someone suggest a way of reducing this to a code sample that shows more usefully the issue, or explain what I have wrong in the above?


A:

Thanks to @abarnert for guiding me to the solution.
As the tp_clear handler for the <code>PyTypeObject</code> for the weakref proxy triggers a garbage collect, on entering the <code>__del__</code> of the cyclic reference, the cyclic reference is already considered logical dead by the garbage collector and as such, the changes to the latefin reference do not cause the latefin object to be kept alive.
The required solution for the original problem is to use <code>WeakSet</code> instances instead of weak references against the earlyfin object
