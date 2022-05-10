import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(1)
</code>
This is what I want, but I want to do it from the <code>inspect</code> module.
<code>import inspect
@inspect.signature(returns=ctypes.py_object)
def fun():
    return 1
</code>
The problem is that I don't know how to create a type object that will wrap the return value in a <code>ctypes.py_object</code> object.
I can use this to get the type of <code>ctypes.py_object</code> but I don't know how to use it.
<code>&gt;&gt;&gt; type(ctypes.py_object)
&lt;class 'type'&gt;
</code>

