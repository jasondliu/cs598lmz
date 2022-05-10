import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
</code>
This prints <code>1 2</code> as expected.
However, if I try to use <code>s.y</code> before <code>s.x</code> is assigned, I get a <code>Segmentation fault</code> error:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.y = 2
s.x = 1

print(s.x, s.y)
</code>
Why is this?

