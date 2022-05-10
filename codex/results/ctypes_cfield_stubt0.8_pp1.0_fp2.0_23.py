import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

Foo = ctypes.CField

foo = Foo(13)

print(type(foo))
print(foo.value)

print(S.x.from_param(foo))
print(S.x.from_param(foo).value)
</code>
The output is:
<code>&lt;class 'ctypes.c_int'&gt;
13
&lt;__main__.S object at 0x000002592B4FF3D0&gt;
13
</code>

