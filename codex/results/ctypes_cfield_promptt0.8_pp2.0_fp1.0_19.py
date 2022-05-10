import ctypes
# Test ctypes.CField
class FP(ctypes.BigEndianStructure):
    _pack_ = 4
    _fields_ = [('a', ctypes.c_float),
                ('b', ctypes.c_float)]

a = FP(1.1, 2.2)
print(a.a, a.b)

# Test ctypes.CFuncPtr
mylib = ctypes.CDLL('/usr/lib/libSystem.dylib')
def print_int(i):
    print('%d\n' % i)
PRINT_INT = ctypes.CFUNCTYPE(None, ctypes.c_int)(print_int)

# Test ctypes.CString
print(mylib.getpid())
mylib.c_print_int(mylib.getpid())
mylib.c_print_int.argtypes = [ctypes.c_int]
mylib.c_print_int.restype = ctypes.c_char_p

# Test ctypes.create_string_buffer
def c_print(string):
    print('%s\n
