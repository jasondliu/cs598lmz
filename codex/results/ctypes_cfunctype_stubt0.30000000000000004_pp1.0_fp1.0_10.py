import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This works fine, but I want to be able to pass a function as an argument to <code>ctypes.CFUNCTYPE</code> and have it return a function of the same type.
<code>def fun2(fun):
    return fun

print(fun2(fun))
</code>
This fails with <code>TypeError: 'CFUNCTYPE' object is not callable</code>. I can get around this by using a <code>ctypes.POINTER</code> to a <code>ctypes.CFUNCTYPE</code>, but I'm not sure how to use it.
<code>def fun3(fun):
    return ctypes.cast(fun, ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.py_object)))

print(fun3(fun))
</code>
This returns a pointer, but I'm not sure how to use it. I've tried <code>fun3(fun)()</code> and <code>fun3(fun).contents()</code>,
