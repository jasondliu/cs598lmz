import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
</code>
This works fine in CPython 3.3, but fails in PyPy:
<code>&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;&gt;&gt; fun()
42
&gt;
