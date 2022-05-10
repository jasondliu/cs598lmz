import ctypes
ctypes.cast(ctypes.c_int(1), ctypes.POINTER(ctypes.c_int))
</code>
I'm running Python 2.7 on Ubuntu 12.04.


A:

It works for me.
I get this:
<code>&lt;__main__.LP_c_int object at 0x7f9e9a2b71e0&gt;
</code>

