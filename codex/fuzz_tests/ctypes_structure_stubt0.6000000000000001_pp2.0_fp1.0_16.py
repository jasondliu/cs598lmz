import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double

a = S()
a.x = 3.
a_ref = ctypes.byref(a)
print a_ref.contents.x

a_ref.contents.x = 4.
print a.x
</code>

