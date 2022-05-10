import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.x
print s.y
</code>
I get the following error:
<blockquote>
<p>AttributeError: 'c_int' object has no attribute 'x'</p>
</blockquote>


A:

You need to use <code>ctypes.c_int(0)</code> to initialize the <code>c_int</code> values.
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print s.x
print s.y
</code>

