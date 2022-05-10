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

"""

def test_late_function_call_with_cyclic_dependency():
    """
    >>> test_late_function_call_with_cyclic_dependency.__doc__.strip()
    '42'
    """

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
    return 42

def test_nested_late_function_call_with_cyclic_dependency():
    """
   
