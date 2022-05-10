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

if __name__ == '__main__':
    import sys
    if sys.flags.debug:
        print('This test is not meant to be run with debug enabled')
        sys.exit(1)
    if func is not None:
        print('func is not None')
        sys.exit(1)
    if latefin is not None:
        print('latefin is not None')
        sys.exit(1)
    print('done')
