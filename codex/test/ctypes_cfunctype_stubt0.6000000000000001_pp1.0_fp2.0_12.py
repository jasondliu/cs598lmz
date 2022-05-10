import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "works"

s = fun()
print(s)

# # On my machine, this also works:
# fun.restype = ctypes.py_object
# s = fun()
# print(s)
