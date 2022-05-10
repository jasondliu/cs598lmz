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

def tee(iterable):
    it = iter(iterable)
    def gen1():
        for x in it:
            yield x
    def gen2():
        for x in it:
            yield x
    return gen1(), gen2()

a, b = tee([1, 2, 3])

print(a.__module__.__class__.__name__)
print(b.__module__.__class__.__name__)

del a, b
gc.collect()

for i in range(10):
    print(latefin.ref())

del latefin
gc.collect()

for i in range(10):
    print(func())
