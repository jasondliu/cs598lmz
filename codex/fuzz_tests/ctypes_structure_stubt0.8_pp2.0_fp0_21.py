import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte
    z = ctypes.c_ubyte[4]
</code>
This is not a clever thing to do in Python - you can also create e.g. a list of three integers:
<code>s = [1, 2, 3, 4, 5, 6]
</code>
But I like the C syntax.
I can access <code>s.x</code> and <code>s.y</code> directly:
<code>&gt;&gt;&gt; s.x
1
&gt;&gt;&gt; s.y
2
</code>
but I have to convert <code>s.z</code> to a list to get the values out of it:
<code>&gt;&gt;&gt; list(s.z)
[3, 4, 5, 6]
</code>
Is there a way to access that data without converting to a list or tuple?
I'm interested in this from a performance point of view - I'm using this to construct and decon
