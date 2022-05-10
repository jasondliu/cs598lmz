import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return True
#fun
#AttributeError: 'NoneType' object has no attribute '__call__'
</code>
What did I do wrong?


A:

Using a <code>ctypes.WINFUNCTYPE</code> is perhaps clearest:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; fun = ctypes.WINFUNCTYPE(ctypes.py_object, *[ctypes.py_object] * 35)()
&gt;&gt;&gt; fun
&lt;ctypes.PyCFuncPtrType object at 0x10a3e4700&gt;
</code>
The <code>*[ctypes.py_object] * 35</code> part is a hack for generating a list in a loop, but it is equivalent to <code>[ctypes.py_object] * 35</code>.

The problem you were having was that <code>ctypes.CFUNCTYPE(ctypes.py_object)</code> creates a type object, not an instance of the type. Python knows to
