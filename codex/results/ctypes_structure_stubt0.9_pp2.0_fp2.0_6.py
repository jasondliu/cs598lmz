import ctypes

class S(ctypes.Structure):
    x = None

S._fields_ = [('x',
               ctypes.POINTER(ctypes.c_void_p)),
              ('y', ctypes.c_int)]
</code>
This works without error
<code>&gt;&gt;&gt; S()
&lt;__main__.S object at 0x10036cde8&gt;
</code>
But I can't figure out how to access the fields
<code>&gt;&gt;&gt; v = S()
&gt;&gt;&gt; v.x
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'S' object has no attribute 'x'
&gt;&gt;&gt; v.y
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'S' object has no attribute 'y'
</code>
What's the proper way to access the fields
