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

"""

# ____________________________________________________________

def test_weakref_to_function():
    """
    >>> import weakref, gc
    >>> def f(): pass
    >>> r = weakref.ref(f)
    >>> r() is f
    True
    >>> del f
    >>> gc.collect()
    0
    >>> r() is None
    True
    """

def test_weakref_to_method():
    """
    >>> import weakref, gc
    >>> class A:
    ...     def m(self): pass
    >>> a = A()
    >>> r = weakref.ref(a.m)
    >>> r() is a.m
    True
    >>> del a
    >>> gc.collect()
    0
    >>> r() is None
    True
    >>> class B:
    ...     def m(self): pass
    >>> b = B()
    >>> r = weakref.ref(b.m)
    >>> r() is b.m
    True
    >>>
