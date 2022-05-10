import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(None)
</code>
And then I get the output:
<code>&gt;&gt;&gt; fun()
&lt;NULL&gt;
&gt;&gt;&gt; fun() is None
False
&gt;&gt;&gt; fun() is object()
False
</code>
My first thought was to use <code>ctypes.cast(fun(), ctypes.c_void_p).value</code>, but that returns 0, not <code>&lt;NULL&gt;</code>.
My question is how can I assign a variable to a PyObject* that points to <code>&lt;NULL&gt;</code>?


A:

You don't need a variable to achieve this. Just use <code>ctypes.py_object(None)</code>.
In the following example, I call function <code>fun()</code> twice and compare the result to <code>ctypes.py_object(None)</code>:
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ct
