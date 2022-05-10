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

# The following test case was reported by Serhiy Storchaka in issue #16033
# and is a reduced version of a test case in the unittest library.

class TestCycle(object):
    def __init__(self):
        self.__dict__['_TestCycle__cycle'] = self

    # This is an implicit test for the pure Python version of
    # object.__setattr__(), since it is called by the implicit call of
    # object.__delattr__() below.  The C version of object.__setattr__()
    # bypasses object.__setattr__() in this case.
    def __delattr__(self, name):
        del self.__dict__[name]

TestCycle()

# This test case was reported by Serhiy Storchaka in issue #16033
# and is a reduced version of a test case in the unittest library.
# It tests that the __del__ method of a class instance is called
# during the collection of a reference cycle.

class TestFinalizer:
