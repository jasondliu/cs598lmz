import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x, s.y

s.x = 3
print s.x, s.y
</code>
Output:
<code>1 2
3 2
</code>
This is because <code>ctypes.c_int()</code> returns a new <code>c_int</code> instance each time.

