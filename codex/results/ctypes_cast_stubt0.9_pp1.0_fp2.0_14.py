import ctypes
ctypes.cast(1, ctypes.c_void_p)
</code>
This gives me a segmentation fault (even if I use <code>c_int.from_address(id(1))</code>).
Of course I can subclass ctypes to implement c_void_p, but the type is probably not well-defined when the value is not the adress of an object. Assuming I want to do this just by using ctypes, how can I proceed?


A:

<code>&gt;&gt;&gt; class X(ctypes.Structure):
...     _fields_ = [('data',ctypes.c_long)]
&gt;&gt;&gt; c_long.from_address(id(1))
c_long(1)
&gt;&gt;&gt; ctypes.cast(id(1),ctypes.POINTER(X)).contents.data
1
</code>

