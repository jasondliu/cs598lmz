import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2, 3)

x = fun()
print(x)
print(type(x))
</code>
output:
<code>(1, 2, 3)
&lt;class 'ctypes.c_int'&gt;
</code>
It seems that <code>ctypes.py_object</code> is the same as <code>ctypes.c_int</code> in this case.
How can I get the correct <code>tuple</code> type?


A:

The problem is that in Python 2, <code>ctypes.py_object</code> is not a pointer to a <code>PyObject</code> but a <code>PyObject</code> itself. This is documented in the <code>ctypes</code> documentation:
<blockquote>
<p>In Python 2.x, <code>&lt;code&gt;ctypes.py_object&lt;/code&gt;</code> is a <code>&lt;code&gt;PyObject&lt;/code&gt;</code>, not a pointer to
