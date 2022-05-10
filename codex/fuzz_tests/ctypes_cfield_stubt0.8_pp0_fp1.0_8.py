import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(S.x.__class__.__base__.__base__)
print(S.x.__class__.__base__)
</code>
This prints:
<code>&lt;class 'ctypes.CField'&gt;
&lt;class 'ctypes.Field'&gt;
</code>
Similarly, the <code>ctypes.c_int</code> is also a <code>_ctypes._SimpleCData</code>.

