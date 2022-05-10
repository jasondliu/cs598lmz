import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
s.x = 2
print s.x
</code>
The output is 1.
I know ctypes is not a good way to do OO programming in Python.
But I want to know why this happens.
Thanks a lot!


A:

<code>ctypes.c_int(1)</code> is a <code>c_int</code> object, not an <code>int</code> object.  You can't assign to a <code>c_int</code> object.  You need to use the <code>value</code> attribute instead:
<code>s.x.value = 2
</code>

