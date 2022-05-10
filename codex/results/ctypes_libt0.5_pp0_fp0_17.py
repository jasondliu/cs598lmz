import ctypes
ctypes.cdll.LoadLibrary("libc.so.6")
libc = ctypes.CDLL("libc.so.6")

def malloc(size):
    return libc.malloc(size)

class my_struct(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = my_struct()
print(s)
s_p = ctypes.pointer(s)
print(s_p)

s_p = ctypes.cast(malloc(ctypes.sizeof(my_struct)), ctypes.POINTER(my_struct))
print(s_p)
s_p.contents.x = 1
s_p.contents.y = 2
print(s_p.contents)
