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
gc.collect()
del latefin

# This should be the last test.
class Final:
    __slots__ = ()
    def __del__(self):
        pass

def final_test(x):
    print(x)

x = Final()
x.__class__ = Final
x.__del__ = final_test
del x
gc.collect()

# This should be the last test.
class Final2:
    __slots__ = ()
    def __del__(self):
        pass

def final_test2(x):
    print(x)

x = Final2()
x.__class__ = Final2
x.__del__ = final_test
del x
