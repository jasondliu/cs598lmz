import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(3)

s = S()

print(s.x)
print(ctypes.sizeof(s))
print(ctypes.sizeof(s.x))
</code>
Outputs:
<code>3
4
4
</code>
But when I put <code>x</code> in a union, it changes size:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('u', ctypes.Union)]
    u = ctypes.Union([('x', ctypes.c_int)])
    u.x = 3

s = S()

print(s.x)
print(ctypes.sizeof(s))
print(ctypes.sizeof(s.x))
</code>
Outputs:
<code>3
0
4
</code>
Why does the union make the structure zero sized?


A:

The problem is that your union is not properly initialized.
Your code:
<code>class S(ctypes.Structure):
    _
