import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2
    z = ctypes.c_char * 2

s = S()

s.x = 'a'
s.y = 'b'
s.z = 'c'

print(s.x)
print(s.y)
print(s.z)

print(ctypes.sizeof(s))
</code>
I would expect this to print
<code>ab
ab
ab
2
</code>
However, it prints
<code>ab
ab
c
3
</code>
Why is this?


A:

I believe the reason is that <code>ctypes.Structure</code>s are packed by default. If you change the <code>S</code> class definition to the following, you'll get the expected output:
<code>class S(ctypes.Structure):
    _pack_ = 1
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2
    z = ctypes.c_char
