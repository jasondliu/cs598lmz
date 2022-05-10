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

def f():
    """
    >>> gc.collect()
    0
    >>> f()
    42
    """
    return 42

def g():
    """
    >>> gc.collect()
    0
    >>> g()
    42
    """
    return 42

def h():
    """
    >>> gc.collect()
    0
    >>> h()
    Traceback (most recent call last):
    ...
    AttributeError: 'int' object has no attribute '__module__'
    """
    return 42

def i():
    """
    >>> gc.collect()
    0
    >>> i()
    42
    """
    return 42

def j():
    """
    >>> gc.collect()
    0
    >>> j()
    42
    """
    return 42

def k():
    """
    >>> gc.collect()
    0
    >>> k()
    >>>
    """
    return 42

def l():
    """
    >>> gc.collect()
    0
    >>>
