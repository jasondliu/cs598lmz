import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p
    z = ctypes.c_char_p
    __slots__ = ('x', 'y', 'z')

s = S()
s.z = 'world'
s.y = 'hello'
s.x = 'world'
print s.x
print s.y
print s.z
</code>

