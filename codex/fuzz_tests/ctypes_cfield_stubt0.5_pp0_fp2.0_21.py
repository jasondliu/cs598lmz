import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C._fields_)
print(C.x)
print(C.x.__class__)
print(C.x.type)
</code>
Output:
<code>[('x', &lt;class 'ctypes._CField'&gt;)]
&lt;class 'ctypes._CField'&gt;
&lt;class 'ctypes._CField'&gt;
&lt;class 'ctypes.c_int'&gt;
</code>

