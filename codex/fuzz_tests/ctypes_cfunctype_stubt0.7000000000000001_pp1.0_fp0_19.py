import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
</code>
Would be nice if this is possible without ctypes.


A:

You can use a <code>lambda</code> function:
<code>&gt;&gt;&gt; type(lambda: 1)
&lt;type 'function'&gt;
</code>
Note however that this is a new function object each time you call <code>type</code>, which isn't the case for your <code>fun</code> - I'm not sure what you're trying to achieve, but it might be worth showing your actual code.

