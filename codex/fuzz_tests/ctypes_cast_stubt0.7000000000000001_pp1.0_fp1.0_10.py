import ctypes
ctypes.cast(0x123, ctypes.c_void_p)

# in PyPy
&lt;cdata 'void *' 0x123&gt;

# in CPython 3.7
c_void_p(291)

# in CPython 2.7
c_void_p(291L)
</code>

