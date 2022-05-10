import ctypes
ctypes.cast(c_p, ctypes.POINTER(ctypes.c_long))
</code>
You can also cast the primitive pointer to a <code>ctypes</code> type that matches the primitive type. This does not have the "from a numpy array" part, but still:
<code>from numpy.ctypeslib import as_array
a = np.arange(10)
c_p = a.ctypes.data_as(ctypes.POINTER(ctypes.c_long))
as_array(c_p, shape=a.shape)
</code>

