import ctypes
ctypes.cast(self.glare.glare_angle.row.value, ctypes.c_void_p)
</code>
Next, once we have the pointer to the data, we can just copy it over to an array that is declared to be of type <code>c_ubyte</code> via <code>memmove</code>. And once you copy the <code>c_ubyte</code> data in the pinned array, you can then reshape this data to the original dimensions. The result of this reshape will be a numpy array with the same data type as the original. So, basically you're copying the data from ctypes pointer to a numpy array with the same data type as the original using pinned memory:
<code>import numpy as np
from numpy.ctypeslib import as_ctypes
from ctypes import c_ubyte, POINTER, memmove, c_void_p

original_shape = (2, 3)
arr = np.ones(original_shape).view(dtype=np.uint8)

ptr = ctypes.cast(arr.ctypes.data, c_void_
