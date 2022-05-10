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
del func, cyc, tb
gc.collect()
del latefin

a = []
for x in range(10):
    a.append(1)
    gc.collect()
    print(a)
    if len(a) == 5:
        a.append(a)

print('*' * 33)

gc.disable()
a = []
for x in range(10):
    a.append(1)
    gc.collect()
    print(a)
    if len(a) == 5:
        a.append(a)
