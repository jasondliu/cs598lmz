import ctypes
ctypes.cast(0, ctypes.py_object)

def f():
    pass

def g(x):
    return x

def h(x):
    try:
        return x
    except:
        pass
    finally:
        pass

def i(x):
    try:
        pass
    except:
        pass
    finally:
        return x

def j(x):
    try:
        return x
    finally:
        pass

def k(x):
    try:
        pass
    finally:
        return x

def l(x):
    def inner():
        return x
    return inner

def m(x):
    class Inner:
        def inner(self):
            return x
    return Inner()

def n(x):
    class Inner:
        def __init__(self):
            self.x = x
        def inner(self):
            return self.x
    return Inner()
