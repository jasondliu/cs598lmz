import ctypes
ctypes.cast(None, PVIEW)
</code>
I'm assuming that in both of these, the type is set to <code>ctypes.c_void_p</code>, so it would be best to just define it that way.

