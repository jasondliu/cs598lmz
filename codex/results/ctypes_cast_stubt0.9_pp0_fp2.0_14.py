import ctypes
ctypes.cast(l, ctypes.c_void_p).value
</code>
<code>&gt;&gt;&gt; 9299664
</code>
Is the memory re-use done in the low level implementation of Python or by the C memory management libraries? How can the address be the same after list destruction?

