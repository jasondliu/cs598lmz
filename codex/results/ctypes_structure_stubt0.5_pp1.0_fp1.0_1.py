import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    y = ctypes.c_void_p

s = S()
s.x = ctypes.cast(s, ctypes.c_void_p)
s.y = ctypes.cast(s, ctypes.c_void_p)

print(s.x == s.y)
</code>
This code prints <code>True</code>.

