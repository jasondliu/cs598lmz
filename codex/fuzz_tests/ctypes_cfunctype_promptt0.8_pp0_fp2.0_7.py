import ctypes
# Test ctypes.CFUNCTYPE

f = ctypes.CFUNCTYPE(ctypes.py_object)
assert f() is None
f = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
assert f("spam") == "spam"
assert f() is None
f = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
assert f("spam", "eggs") == "spam"
assert f() is None

# A function that takes no arguments and returns an integer
f1 = ctypes.CFUNCTYPE(ctypes.c_int)

# A function that takes an integer argument and returns an integer
f2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

code = """
def f1(x):
    return x + 1

def f2(x):
    return 2*x

def f3(x):
    return f1(x) + f2(x)
"""
