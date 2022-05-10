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
sys.getrefcount(latefin)    # keep latefin alive

gc.collect()        # kills all but one of `cyc`
del latefin
</code>

The issue with your case is that it never called <code>__del__</code> so the <code>instancemethod</code> object was never modified to refer to the living <code>latefin</code> object.
Maybe having a <code>__del__</code> method that performs the modification to <code>self.ref</code> and then does the <code>del latefin</code> would be good for the case when it gets called:
<code>class Untracked(object):
    __slots__ = ('ref',)
    def __del__(self):
        global latefin
        self.ref = latefin
        del latefin

class Tracked(object):
    def __init__(self):
        self.untracked = Untracked()
        self.untracked.ref = self
        del self
</code>

You can get a cycle in the normal way by using a
