import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
x = fun()
def handle_return_int(value):
    return x.rget()
globals()["a"] = handle_return_int
assert a() == -1
def handle_return_obj(value):
    if isinstance(value, ctypes.py_object):
        return x.rget()
    return value
globals()["b"] = handle_return_obj
assert b(1) == -1
def handle_return_int_obj(value):
    if isinstance(value, ctypes.py_object):
        return x.rget()
    return 2
globals()["c"] = handle_return_int_obj
assert c(1) == 2
def handle_return_bool(value):
    if isinstance(value, ctypes.py_object):
        return bool(x.rget())
    return [1, 0][bool(value)]
globals()["d"] = handle_return_bool
assert d(1) == 1

h = 0
def handle_return_obj_2
