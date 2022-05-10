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

m = sys.modules['__main__']
m.__setattr__('__file__', '&lt;string&gt;')

print('done')
</code>
This is a simplified version of the code that crashes.  It does not reproduce the crash for me.  However, I have been able to reproduce the crash with a slightly more complicated version of the code that I can't share here.

