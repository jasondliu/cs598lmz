import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class R(ctypes.Structure):
    _fields_ = [('_', ctypes.c_void_p),
                ('x', ctypes.c_int),
                ('y', ctypes.c_int)]

s = S(x = 1, y = 2)
r = R(x = 1, y = 2)

print ctypes.c_void_p.from_buffer(s).value == ctypes.addressof(s)
print ctypes.c_void_p.from_buffer(r).value != 0
print ctypes.c_void_p.from_buffer(r).value != ctypes.addressof(r)
</code>
The type conversion works for <code>S</code>, but fails for <code>R</code>. Is there any way I can get the pointer to a C-structure's memory from Python?
Edit: I went on and did <code>id(s)</code>, which is what I really wanted. Is this really the only way to get a number
