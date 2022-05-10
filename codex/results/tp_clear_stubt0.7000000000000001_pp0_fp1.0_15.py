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
del func, cyc, latefin

gc.collect()

def run():
    print "Hello world"

func()
</code>
I've tested it with python 2.6.7 and 2.7.3, so I'm not sure that it is a bug.
PS: I've added <code>__slots__</code> to classes to minimize memory usage.


A:

The <code>gc</code> module is pretty complicated, so much so that I don't think it's easy to predict what will happen.  It's not a bug.  The <code>__del__</code> method of <code>LateFin</code> is executed, and the reference remains alive.  The <code>__del__</code> method of <code>Cyclic</code> is not executed because <code>LateFin</code> is still alive, and <code>ref</code> is not set.  The <code>__del__</code> method of <code>LateFin</code> is also not executed because <code>Cyclic</code> is still alive.
The <code>__del__</code
