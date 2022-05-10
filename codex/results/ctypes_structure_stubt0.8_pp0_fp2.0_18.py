import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.0)

s = S()
print("Original:", s.x)
double_ptr = ctypes.cast(ctypes.byref(s), ctypes.POINTER(ctypes.c_double))
double_ptr[0] = 3.0
print("Changed:", s.x)
</code>
Obviously, it is possible to use this approach to modify any member of the structure that is not a function.

I'm not quite sure what you mean by "a pointer to the function member". But the function itself can't be passed to <code>cast</code> because it's not a <code>ctypes</code> object.

