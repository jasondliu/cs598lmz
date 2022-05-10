import weakref
# Test weakref.ref() and weakref.proxy()

class Foo:
    def __del__(self):
        print("Foo.__del__")

def bar():
    print("Bar")

class Client:
    def __init__(self, obj):
        self._obj = obj

    def __del__(self):
        self._obj()

def test_ref():
    # Refs to objects are created by the ref() function, and can be passed around
    # like any other object, but the referent is reference counted (see
    # PyObject_GC_UnTrack() in the C implementation for details).
    # The referent is not collected until the refcount reaches zero.
    f = Foo()
    f_ref = weakref.ref(f)
    f_ref()
    del f
    assert f_ref() is None

    # A reference to a function
    f = bar
    f_ref = weakref.ref(f)
    f_ref()
    del f
    assert f_ref() is None

    # A reference to a callable object
    f
