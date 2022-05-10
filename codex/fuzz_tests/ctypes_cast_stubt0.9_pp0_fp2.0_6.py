import ctypes
ctypes.cast(X.ctypes.data, ctypes.POINTER(np.ctypeslib.ndpointer(dtype=np.float32,
                                                                 ndim=2,
                                                                 shape=(1, 13))))
</code>
Now <code>X</code> also points to <code>Y</code>. The <code>shape</code> parameter is used by <code>np = import ctypes</code>.
Still I think you should define the entire matrix as output argument and then feed it to the DLL.

