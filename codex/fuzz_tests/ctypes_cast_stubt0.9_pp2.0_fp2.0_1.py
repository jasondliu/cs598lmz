import ctypes
ctypes.cast(ptr, ctypes.POINTER(Type*N))
</code>
With <code>ctypes</code>, use <code>from_address</code>:
<code>&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; from ctypes.util import find_library
&gt;&gt;&gt; libc = cdll.LoadLibrary(find_library('c'))
&gt;&gt;&gt; libc.calloc.argtypes = [c_size_t, c_size_t]
&gt;&gt;&gt; libc.calloc.restype = c_void_p
&gt;&gt;&gt; libc.calloc(5, sizeof(c_double)).from_address(libc.calloc.restype(libc.calloc.argtypes))
</code>
Note that <code>from_address</code> takes an address, not a pointer type.

