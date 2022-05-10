import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def f():
    return "hello"

def g():
    return "world"

def h():
    return "!"

def fg():
    return f() + g()

def fgh():
    return fg() + h()

def fgh_nested():
    return f() + g() + h()

def fgh_nested_2():
    return f() + (g() + h())

def fgh_nested_3():
    return (f() + g()) + h()

def fgh_nested_4():
    return (f() + g() + h())

def fgh_nested_5():
    return ((f() + g()) + h())

def fgh_nested_6():
    return (f() + (g() + h()))

def fgh_nested_7():
    return ((f() + g()) + h())

def fgh_nested_8():
    return (f() + (g() + h()))

