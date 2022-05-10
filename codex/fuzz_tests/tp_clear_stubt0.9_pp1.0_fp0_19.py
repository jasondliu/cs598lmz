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
Can anyone help me debug the crash?  Platform is Linux 64, Ubuntu 11 with Python 2.7.3 as packaged by Ubuntu.
My next question is: Why isn't Python catching this crash?


A:

This crash seems to be a known issue caused by the standard Python interpreter using pymalloc on 64-bit platforms.  There is a cryptic note in the source about pymalloc not yet supporting 64-bit platforms.  This is not a problem on 32-bit platforms where Python uses non-pymalloc malloc.

