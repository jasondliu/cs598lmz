import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p
    z = ctypes.c_char_p

s = S()
s.x = ctypes.c_char_p(b'x')
s.y = ctypes.c_char_p(b'y')
s.z = ctypes.c_char_p(b'z')
print s.x, s.y, s.z
</code>
Output:
<code>x y z
</code>

