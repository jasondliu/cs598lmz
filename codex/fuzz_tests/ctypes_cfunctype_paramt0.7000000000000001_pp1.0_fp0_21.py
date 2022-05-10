import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_int,ctypes.c_int)
f = ctypes.CDLL('./libc.so')
c = ctypes.c_double(1.0)
l = FUNTYPE(lambda x,y: x + y)
f.foo(c,l,1,2)
</code>
In fact, if I try to use <code>l</code> returned by <code>FUNTYPE</code> directly, it would fail:
<code>l(1,2)
</code>
gives me the error
<code>TypeError: '_FuncPtr' object is not callable
</code>
<code>f.foo(c,l(1,2),1,2)</code> doesn't work either with the error:
<code>TypeError: this type has no size
</code>
However, if I use a <code>ctypes.CFUNCTYPE</code> which has no return value, I can use it directly:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE
