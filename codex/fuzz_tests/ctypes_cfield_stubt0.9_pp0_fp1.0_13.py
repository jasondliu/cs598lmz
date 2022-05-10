import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFieldSubtype(ctypes.CField):
    pass

class St(ctypes.Structure):
    _fields_ = [('f', CFieldSubtype)]

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.malloc.argtypes = (ctypes.c_size_t,)
libc.malloc.restype = ctypes.c_void_p

s = ctypes.POINTER(S)(S(ffi=ctypes.FFI().from_handle(libc._handle)))
st = libc.malloc(ctypes.sizeof(S) + 100)
s[0].x = 42
print(s[0].x)  # 42
print(s)
print(t)

t = St.from_buffer(st)
t.f = 42
print(s.contents)
ffi = ctypes.FFI().from_handle(libc._handle)
print(ffi.string(ffi.cast('char *', st)))
libc.free(
