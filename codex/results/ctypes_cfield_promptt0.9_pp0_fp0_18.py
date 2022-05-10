import ctypes
# Test ctypes.CField.from_param

class U(ctypes.Union):
    _fields_ = [("c", ctypes.c_char),
                ("i", ctypes.c_int)]

u = U()
u.c = b'c'

for param in [u.c, ctypes.c_char.from_param(u.c)]:
    ctypes.string_at(param)

for param in [u.i, ctypes.c_int.from_param(u.i)]:
    x = ctypes.cast(param, ctypes._pointer_t(ctypes.c_char))

try:
    ctypes.string_at(u.i)
except TypeError as e:
    if not 'argument 1 must be str, not c_int' in str(e):
        raise Exception("wrong error")

try:
    x = ctypes.cast(u.c, ctypes._pointer_t(ctypes.c_char))
except TypeError as e:
    if not 'argument 1 must be LP_c_char, not c_char
