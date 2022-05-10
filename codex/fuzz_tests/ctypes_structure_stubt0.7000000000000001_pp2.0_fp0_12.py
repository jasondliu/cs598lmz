import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16
    y = ctypes.c_uint16

s = S()
id(s.x) == id(s.__dict__['x'])

True
</code>
This means that <code>ctypes</code> doesn't really hide its fields behind the <code>__dict__</code> attribute.
You can't say the same about <code>cffi</code>. If you create a simple <code>cffi</code> structure, it will work like the one from <code>ctypes</code>:
<code>from cffi import FFI
ffi = FFI()
ffi.cdef('typedef struct { int x; int y; } S;')
s = ffi.new('S *')
id(s.x) == id(s.__dict__['x'])

True
</code>
However, it is possible to create a structure which won't have its fields in the <code>__dict__</code> by declaring it in the following way:
<code>ffi.cdef('typedef struct
