import ctypes
ctypes.cast(None, ctypes.c_void_p).value
# 0
ctypes.cast(lambda: None, ctypes.c_void_p).value
# 140735182978944
ctypes.cast(Exception(), ctypes.c_void_p).value
# 140735182978992
ctypes.cast(tuple(), ctypes.c_void_p).value
# 140447210718496
ctypes.cast(list(), ctypes.c_void_p).value
# 140447210718848
ctypes.cast(dict(), ctypes.c_void_p).value
# 140447210726384
def foo():
    pass
ctypes.cast(foo, ctypes.c_void_p).value
# 140735182978992
</code>
So it appears that <code>ctypes.cast(None, ctypes.c_void_p)</code> returns a pointer to the address <code>0</code> while <code>ctypes.cast(foo, ctypes.c_void_p)</code> returns a pointer to the address
