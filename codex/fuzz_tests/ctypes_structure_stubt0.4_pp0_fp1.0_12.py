import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

s2 = S()
s2.x = 3
s2.y = 4
print(s2.x, s2.y)

print(s.x, s.y)
</code>
Output:
<code>1 2
3 4
1 2
</code>
What I want is for the output to be
<code>1 2
3 4
3 4
</code>
I believe that the problem is that the structure is being copied. Is there a way to avoid this?


A:

You can use <code>byref</code> to pass a pointer to the structure instead of a copy of the structure.
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

s = S()
s.x = 1
s
