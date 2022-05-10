import ctypes
ctypes.cast(
    ctypes.cast(
        ctypes.c_void_p(0),
        ctypes.POINTER(ctypes.c_void_p)
    ).contents, 
    ctypes.POINTER(foo)  # type: ignore
).contents.x
</code>

