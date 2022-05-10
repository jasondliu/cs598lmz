import ctypes
ctypes.cast(ctypes.c_void_p(py_array.ctypes.data), ctypes.POINTER(ctypes.c_float))
</code>
But is there a way to do this directly in numpy?


A:

You can use <code>np.ctypeslib.as_ctypes</code> to get a ctypes pointer to the data without copying.
<code>import numpy as np
import ctypes

a = np.array([1, 2, 3, 4], dtype=np.float32)
c_float_p = ctypes.cast(np.ctypeslib.as_ctypes(a), ctypes.POINTER(ctypes.c_float))
</code>

