import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
fun()
</code>
I get
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: an integer is required (got type NoneType)
</code>
I tried <code>ctypes.py_object(0)</code> and <code>ctypes.py_object(None)</code> but they don't work either.
I am on Python 3.6.8. Any idea?


A:

You are missing a <code>return</code> statement.
<code>&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
&gt;&gt;&gt; @FUNTYPE
... def fun():
...     return 0
... 
&gt;&gt;&gt; fun()
0
</code>

