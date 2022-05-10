import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
print s.x, s.y

s2 = S()
s2.x = 3
s2.y = 4
print s2.x, s2.y

s3 = S()
s3.x = 5
s3.y = 6
print s3.x, s3.y
</code>
This is what I get:
<code>1 2
3 4
5 6
</code>
This is what I expect:
<code>1 2
3 2
5 6
</code>
I've tried calling <code>__init__</code> but that didn't help.
How do I get the expected output?


A:

<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
</code>

