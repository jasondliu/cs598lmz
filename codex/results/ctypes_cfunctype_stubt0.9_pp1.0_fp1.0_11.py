import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

TypeError: Don't know how to convert parameter 2
</code>

I thought <code>ctypes.py_object</code> were the correct type. Is it wrong ?
Is it possible to call the function, or to wrap it in a <code>ctype</code> compatible type, without modifying the function ? It's a function defined in Cython to be used by Python.



A:

Python objects aren't compatible with <code>ctypes</code>. As the documentation states:
<blockquote>
<p>The <code>&lt;code&gt;ctypes&lt;/code&gt;</code> module provides a simple way to create and manipulate C data types in Python. It can be used to wrap these libraries in pure Python.</p>
</blockquote>
To get Python objects out of C, you have to build the results in a compatible way, likely using <code>Py_BuildValue()</code> in C.
If that's not possible, you could use the Python C API directly to call the function without <code>ctypes</code>.

