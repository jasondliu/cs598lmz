import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()

S.x.offset = lambda obj: ctypes.addressof(obj)
S.y.offset = lambda obj: ctypes.addressof(obj) + ctypes.sizeof(ctypes.c_float)

s = S()
s.x = 1.0
s.y = 2.0

print [ctypes.cast(ctypes.addressof(s) + i, ctypes.POINTER(ctypes.c_float)).contents.value for i in range(ctypes.sizeof(S))]
</code>
I can't understand why it doesn't work.


A:

You can't do that.  The <code>offset</code> attribute is used when you have a <code>ctypes.Array</code> of <code>S</code> objects and you want to access the <code>x</code> and <code>y</code> members of the array elements.
Here's the docs for <code>offset</code>:
<blockquote>
<p
