import _struct
print(max(_struct.unpack(">f", _struct.pack(">f", 1e+50))))  # works
print(max(_struct.unpack(">d", _struct.pack(">d", 1e+300))))  # works
print(max(float(1e+300), "float"))  # does not work (infinite loop)
print(max(float(1e+300), float(1e+300)))  # does not work (infinite loop)
""")
</code>


A:

This is usually a bug in the implementation of the cmp function of the library. This function is automatically used by min and max.
<code>&gt;&gt;&gt; float('inf')==float('inf')
True
&gt;&gt;&gt; cmp(float('inf'), float('inf'))
0
&gt;&gt;&gt; max(1, 2, float('inf'), float('inf'))
inf
&gt;&gt;&gt; max(1, 2, float('inf'), float('inf'), float('inf'),
