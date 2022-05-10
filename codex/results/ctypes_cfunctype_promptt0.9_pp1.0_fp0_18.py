import ctypes
# Test ctypes.CFUNCTYPE
######################################################################
addressof = ctypes.addressof

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def test(self):
        print("test")
x = X()
y = X()
cdecl = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
p = cdecl(addressof(x.test))

print(addressof(x.test))
print(addressof(y.test))
print(p)
</code>
Output
<code>2115887192
2115887552
&lt;__main__.CFUNCTYPE_cdecl_ret_int(0x7fed3e3b9a40)(0x7fed3e3b9a40, 0x7fed3e3b9a40) object at 0x7fed3e425ac8&gt;
</code>


A:

You have found a very interesting problem.
