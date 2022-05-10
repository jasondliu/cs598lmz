from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.gi_name, a.gi_defaults)
</code>
This gives me the following functions:
<code>In [21]: a
Out[21]: &lt;generator object &lt;genexpr&gt; at 0x0136C5E8&gt;

In [22]: b
Out[22]: &lt;function &lt;genexpr&gt; at 0x0136A0D0&gt;
</code>
What's better, calling <code>a.gi_code</code> or <code>b.func_code</code> will give you the same code object.

1 <code>gi_code</code> is the frame's reference to the code object on which to base the generator.

