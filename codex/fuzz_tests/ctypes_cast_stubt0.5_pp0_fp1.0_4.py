import ctypes
ctypes.cast(ctypes.addressof(instance), ctypes.POINTER(ctypes.c_int))
</code>

The following is a complete example that demonstrates the use of <code>ctypes</code> to access the memory of a <code>numpy</code> array:
<code>import numpy as np
import ctypes
from ctypes import c_int, POINTER

def print_memory(arr):
    print('buffer:', arr.__array_interface__['data'])
    print('ctypes:', ctypes.addressof(arr))
    print('ctypes:', ctypes.addressof(arr.ctypes.data_as(POINTER(c_int))))
    print('ctypes:', ctypes.addressof(arr.ctypes.data_as(POINTER(c_int)).contents))

print('\n--- Create array (C-contiguous) ---')
arr = np.array([1, 2, 3], dtype=np.int32)
print_memory(arr)

print('\n--- Create array (F-contiguous
