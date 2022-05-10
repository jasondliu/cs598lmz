import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

r = fun()
assert r == "hello"

# issue #1810: crash in ctypes.CFUNCTYPE()

