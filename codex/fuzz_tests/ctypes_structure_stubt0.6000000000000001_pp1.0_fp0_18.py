import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

def set_struct(s):
    s.x = 5
    s.y = 6

s = S()
set_struct(s)
print(s.x, s.y)
</code>

