import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    _fields_ = [('value', ctypes.CField)]

a = A(77)
print(a.value)
print(int(ctypes.byref(a.value)))
print(A.value)
print(a.value._type_)
print(ctypes.addressof(a))
</code>
Output:
<code>77
30346623
&lt;Field type=c_int, ofs=0: value&gt;
c_int
30346608
</code>

