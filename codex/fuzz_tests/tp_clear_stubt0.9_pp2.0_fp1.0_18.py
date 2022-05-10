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
</code>
the last line triggers the issue:
<code>Fatal Python error: (pycore) Segmentation fault
Current thread 0x00007f735ef3a740 (most recent call first):
 File "./crash.py", line 22 in main
</code>


A:

This is a python issue https://github.com/python/cpython/issues/17840.

