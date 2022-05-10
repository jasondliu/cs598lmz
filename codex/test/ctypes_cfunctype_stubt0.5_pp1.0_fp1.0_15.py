import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

# @functools.wraps(fun)
# def fun():
#     return 1

print(fun())
