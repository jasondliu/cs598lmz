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

if __name__ == '__main__':
    import sys
    if sys.version_info < (3, 4):
        print('SKIP')
        raise SystemExit

    # Exiting is OK, but it would be better to notify user
    import atexit
    atexit.register(func)
