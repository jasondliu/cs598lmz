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
del func, cyc, LateFin, Cyclic
gc.collect()

func()
"""

def test_simple_finalizer():
    import _testcapi
    # This is a simple test to check that a finalizer can run
    # when there is an exception.  This is important because
    # the exception is caught by the C code and the Python
    # exception info is cleared.
    #
    # The test is in C because the finalizer needs to run
    # during a stack unwind, which can't be forced easily
    # in Python.
    #
    # The function is defined here so that it can be used
    # by test_finalizer_no_exception, below.
    def f():
        pass
    f.func_code = _testcapi.test_finalizer_exc_code()
    _testcapi.test_finalizer_exc(f)

def test_finalizer_no_exception():
    import _testcapi
    # This is a simple test to check that a finalizer can run
    # when there is no exception.  This is important because
