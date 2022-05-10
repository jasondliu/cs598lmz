import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(x=1, y=2)

print(s.x)
print(s.y)
print(s.x + s.y)
</code>
The output is:
<code>1
2
3
</code>
As you can see, the <code>x</code> and <code>y</code> attributes of <code>s</code> are <code>c_int</code> objects.

