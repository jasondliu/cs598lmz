import ctypes
ctypes.cast(X, ctypes.c_void_p).value

#1280
</code>
Note: if <code>X</code> is not a ctypes object, this will raise a <code>TypeError</code>. 

