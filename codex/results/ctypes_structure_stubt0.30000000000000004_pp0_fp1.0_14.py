import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s_p = ctypes.pointer(s)
s_p.contents.x = 3
s_p.contents.y = 4

print s.x, s.y
</code>
Output:
<code>1 2
3 4
</code>

