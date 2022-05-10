import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(msg, *args):
    print(msg)
    for tp, value in args:
        print('%s: %r' % (tp, value))
        print(' ', value.__class__)

test('numbers',
     (ctypes.c_byte, ctypes.c_byte(42)),
     (ctypes.c_ubyte, ctypes.c_ubyte(42)),
     (ctypes.c_short, ctypes.c_short(42)),
     (ctypes.c_ushort, ctypes.c_ushort(42)),
     (ctypes.c_int, ctypes.c_int(42)),
     (ctypes.c_uint, ctypes.c_uint(42)),
     (ctypes.c_long, ctypes.c_long(42)),
     (ctypes.c_ulong, ctypes.c_ulong(42)),
     (ctypes.c_longlong, ctypes.c_longlong(42)),
     (ctypes.c_ulonglong, ctypes
