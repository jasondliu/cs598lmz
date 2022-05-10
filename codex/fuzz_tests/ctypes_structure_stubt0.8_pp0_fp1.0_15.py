import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    y = ctypes.c_double(2.0)
    z = ctypes.c_longlong(3.0)
</code>
When I use the <code>__repr__</code> of this class, I get
<code>&gt;&gt;&gt; S()
&lt;__main__.S object at 0x7f9f942b4a70&gt;
</code>
How can I get this <code>repr</code> to be in a more human-readable and editable form, such as
<code>&gt;&gt;&gt; S()
&lt;__main__.S [1.0, 2.0, 3.0]&gt;
</code>
?
This is a code example of what I have tried so far:
<code>import ctypes
class S(ctypes.Structure):
    x = ctypes.c_float(1.0)
    y = ctypes.c_double(2.0)
    z = ctypes.
