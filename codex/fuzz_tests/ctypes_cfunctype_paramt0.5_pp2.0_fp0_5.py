import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# ctypes.c_int(0) =&gt; 0
# ctypes.c_int(1) =&gt; 1

# ctypes.CFUNCTYPE(ctypes.c_int)(0) =&gt; &lt;class 'ctypes.CFUNCTYPE'&gt;
# ctypes.CFUNCTYPE(ctypes.c_int)(1) =&gt; &lt;class 'ctypes.CFUNCTYPE'&gt;

# ctypes.CFUNCTYPE(ctypes.c_int)(0)(0) =&gt; 0
# ctypes.CFUNCTYPE(ctypes.c_int)(1)(1) =&gt; 1
</code>
So, to get the result you are expecting, you can do:
<code>def get_callback(func):
    return FUNTYPE(func)
</code>

