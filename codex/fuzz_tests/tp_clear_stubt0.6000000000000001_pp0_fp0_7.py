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
latefin.ref()

# ____________________________________________________________

def func_with_docstring(arg):
    """
    This is a docstring
    """
    print arg

def func_with_docstring2(arg):
    """
    This is a docstring
    """
    "and this is not!"
    print arg

def func_with_docstring3(arg):
    """
    This is a docstring
    """
    "and this is not!"
    return arg

def func_with_docstring4(arg):
    """
    This is a docstring
    """
    "and this is not!"
    return arg
    print arg

def func_with_docstring5(arg):
    """
    This is a docstring
    """
    print arg
    "and this is not!"
    return arg

def func_with_docstring6(arg):
    """
    This is a docstring
    """
    print arg
    return arg
    "and this is not!"

def func_
