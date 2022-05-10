import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

a = S()
a.x = 3
print a.x
</code>
It's more typing, but it's less error prone and it's more explicit.

