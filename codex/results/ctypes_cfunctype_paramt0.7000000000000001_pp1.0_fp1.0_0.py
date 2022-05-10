import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
def free():
    fun = FUNTYPE(ctypes.cast(0x004066C9, ctypes.c_void_p).value)
    fun()

print 'free is at', hex(ctypes.cast(free,ctypes.c_void_p).value)
free()
print 'free is at', hex(ctypes.cast(free,ctypes.c_void_p).value)
</code>
On my system, <code>free</code> happens to be at 0x004066C9 (YMMV, but it's probably in the same 0x004xxxxx range).

