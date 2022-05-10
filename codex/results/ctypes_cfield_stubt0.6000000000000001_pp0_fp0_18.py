import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
Now, you can use <code>ctypes.CField</code> and <code>ctypes.CField.from_param</code> for validating parameters:
<code>def f(x: ctypes.CField):
    print(x.value)

f(S.x) # prints 1
</code>
This is equivalent to:
<code>def f(x: ctypes.c_int):
    print(x.value)

f(S.x) # prints 1
</code>

