import ctypes
ctypes.cast(1, ctypes.c_void_p)
</code>
Expected: <code>c_void_p(1)</code>
Actual: <code>c_void_p(&lt;memory at 0x7f8c7b9ce148&gt;)</code>
I've tried to use <code>ctypes.addressof</code> in <code>__repr__</code> but it didn't work.

