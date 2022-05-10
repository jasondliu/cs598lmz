import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long.from_address(id(ctypes.py_object(u'\u1234')))

try:
    th = S()
except TypeError:
    print('TypeError')
