import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int * 2
    y = ctypes.c_int * 2

s = S()
print s.x[0]
print s.y[0]
</code>
This prints
<code>0
0
</code>
as expected.
However, if I change <code>S</code> to
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int * 2), ('y', ctypes.c_int * 2)]
</code>
then I get
<code>0
-1073741824
</code>
Why?


A:

<code>_fields_</code> is a list of tuples, not a dict.  The second element of each tuple is the type.  So, <code>y</code> is a tuple, not an array.  You want to make it a <code>ctypes.Array</code>:
<code>&gt;&gt;&gt; class S(ctypes.Structure):
...     _fields_ = [('x', ctypes
