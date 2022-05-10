import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cb_func = FUNTYPE(lambda a,b: a+b)

cb_func(1,2)
</code>
Now I want to pass this <code>cb_func</code> as a callback function to a C library function named <code>register_callback</code>.
<code>register_callback(cb_func)
</code>
How do I write <code>register_callback</code> in ctypes?


A:

You are very close, this is how you should do it:
<code>&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; import ctypes
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; FUNTYPE = CFUNCTYPE(c_int, c_int, c_int)
&gt;&gt;&gt; FUNTYPE
&lt;class 'ctypes.CFUNCTYPE'&gt;
&
