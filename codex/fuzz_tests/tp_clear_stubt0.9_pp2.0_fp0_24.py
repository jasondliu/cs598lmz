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

# The GC didn't use ref_with_del: the ref has been zeroed
latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))
func.__module__ = cyc
del func, cyc, latefin
gc.collect()
func()


# Retain the object (a PyDescr_COMMON_DESCRIPTOR) after the func
# is deallocated:
class MyGlobal:
    __slots__ = ('x',)

class Metaclass(type):
    __slots__ = ()
    @staticmethod
    def lambda_method():
        return 42
    def __init__(cls, name, bases, dct):
        cls.attr = cls.lambda_method

class Demo(metaclass=Metaclass):
    __slots__ = ()

gc.collect()

# check that the GC is differentiating PyDescr_COMMON_DESCRIPTOR
# and other objects derived from PyObject
module = sys.getrefcount(Dem
