import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello from C!"
</code>
The function <code>fun</code> is a Python function object that can be called from Python.  The function object is also a <code>ctypes.CFUNCTYPE</code> object, which is a C-callable function pointer.  The <code>CFUNCTYPE</code> object has an attribute <code>_ptr</code> that is a <code>ctypes.c_void_p</code> object.  This <code>c_void_p</code> object is a C-callable function pointer.
<code>&gt;&gt;&gt; fun()
'Hello from C!'
&gt;&gt;&gt; fun._ptr
&lt;ctypes.c_void_p object at 0x7f6b5d5a5a60&gt;
&gt;&gt;&gt; fun._ptr.value
139906172589160
</code>
Here's the C code:
<code>void *fun_ptr = (void *)139906172589160;
PyObject
