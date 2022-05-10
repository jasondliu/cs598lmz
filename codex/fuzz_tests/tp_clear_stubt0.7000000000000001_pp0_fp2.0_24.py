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

def test():
    print(latefin.ref is None)

test()
</code>
Output on my Python 3.3 (32-bit):
<code>False
</code>
Output on my Python 3.3 (64-bit):
<code>True
</code>
The behavior seems to be the same on Python 2.7 (both 32-bit and 64-bit).
What's going on here? Why is the cyclic reference breaking in the 64-bit version of Python 3.3, but not in the 32-bit version? Is this a bug?

