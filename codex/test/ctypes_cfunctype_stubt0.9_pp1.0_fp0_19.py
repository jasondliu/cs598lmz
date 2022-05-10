import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
@FUNTYPE
def fun():
    return ()
@FUNTYPE
def fun():
    return []
@FUNTYPE
def fun():
    return [None]
@FUNTYPE
def fun():
    return {}
@FUNTYPE
def fun():
    return 1
@FUNTYPE
def fun():
    return 1.3
@FUNTYPE
def fun():
    return True
@FUNTYPE
def fun():
    return False
@FUNTYPE
def fun():
    return "hello"
@FUNTYPE
def fun():
    return 'hello'
@FUNTYPE
def fun():
    return NotImplemented
@FUNTYPE
def fun():
    return None
@FUNTYPE
def fun():
    return NotImplemented
@FUNTYPE
def fun():
    return []
@FUNTYPE
def fun():
    a = 1
    a = 2
    return a
@FUNTYPE
def fun():
    return 64 ** 100
@FUNTYPE
def fun():
    return 64 & 4
@FUNTYPE
def fun():
    return 64 | 4
