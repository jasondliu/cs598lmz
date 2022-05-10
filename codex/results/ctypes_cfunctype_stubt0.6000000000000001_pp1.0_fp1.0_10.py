import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
print(type(fun))
print(fun.__closure__)
</code>
The output is:
<code>42
&lt;class 'ctypes.CFUNCTYPE'&gt;
None
</code>
As you can see, the type of <code>fun</code> is <code>ctypes.CFUNCTYPE</code>, which is a type of C function, not an ordinary Python function. There is no <code>__closure__</code> in this case.

