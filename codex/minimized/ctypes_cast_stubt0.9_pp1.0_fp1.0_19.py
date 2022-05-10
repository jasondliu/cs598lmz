import ctypes
def to_dict(pyobj):
    pobj =  ctypes.cast(id(pyobj), ctypes.POINTER(ctypes.py_object))[0]
print(
    to_dict({1:2})
)
