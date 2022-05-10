import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   return 3
</code>
Now, if I try to access the <code>__code__</code> attribute of <code>fun</code>, I get the following error:
<code>&gt;&gt;&gt; fun.__code__
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'CFUNCTYPE' object has no attribute '__code__'
</code>
I would like to know why there is no <code>__code__</code> attribute and whether there is any way to access it.

