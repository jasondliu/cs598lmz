import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

# This function should not raise TypeError.
def test_call_with_null_return():
    fun()

class A(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash(self.x)

class B(object):
    def __init__(self, x):
        self.x = x

def test_refcount_dict():
    # Make sure that the refcount of dict keys is not decremented
    # when an item is deleted from it.
    d = {A(1): 1}
    weakref.ref(d)
    del d
    import gc; gc.collect(); gc.collect(); gc.collect()

def test_refcount_set():
    # Make sure that the refcount of set elements is not decremented
    # when an item is deleted from it.
    s = set([A(1)])
    weakref.ref
