import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
	return 3.14
</code>
This is reasonably fast:
<code>In [1]: import ctypes

In [2]: FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

In [3]: @FUNTYPE
   ...: def fun():
   ...:     return 3.14
   ...: 

In [4]: %timeit fun()
10000000 loops, best of 3: 46.3 ns per loop
</code>
Edit: apparently py_object is not much better than object. For completeness, here is a benchmark using bytes instead:
<code>In [5]: FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)

In [6]: @FUNTYPE
   ...: def fun():
   ...:     return b'hello'
   ...: 

In [7]: timeit fun()
10000000 loops, best of 3: 35.7 ns per loop
</code>

