import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

&gt;&gt;&gt; fun.argtypes
( &lt;class 'ctypes.py_object'&gt;,)
&gt;&gt;&gt; fun.restype
&lt;class 'ctypes.py_object'&gt;
&gt;&gt;&gt; fun.__objclass__
&lt;class '__main__.fun'&gt;
&gt;&gt;&gt; fun.__name__
'fun'
</code>

