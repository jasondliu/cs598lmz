import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print(C.x.__class__)
print(type(C.x))
print(C.x.__class__ is ctypes.CField)
print(type(C.x) is ctypes.CField)

try:
    ctypes.CField = type(C.x)
except TypeError:
    print("TypeError")
</code>
Output:
<code>&lt;class 'ctypes._CData_type'&gt;
&lt;class 'ctypes._CData_type'&gt;
True
True
TypeError
</code>

