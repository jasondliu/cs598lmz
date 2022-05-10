import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello world")
    return 1

def fun2(x):
    return x + 1

def fun3(x):
    """
    >>> fun3(3)
    4
    """
    return fun2(x)

def fun4(x):
    """
    >>> fun4(3)
    4
    """
    return fun2(x)

def fun5(x):
    """
    >>> fun5(3)
    4
    """
    return fun2(x)

def fun6(x):
    """
    >>> fun6(3)
    4
    """
    return fun2(x)

def fun7(x):
    """
    >>> fun7(3)
    4
    """
    return fun2(x)

def fun8(x):
    """
    >>> fun8(3)
    4
    """
    return fun2(x)

def fun9(x):
    """
    >>> fun9(3)
    4
    """
    return fun2(x)
