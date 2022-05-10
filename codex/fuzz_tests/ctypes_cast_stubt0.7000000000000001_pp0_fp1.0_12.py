import ctypes
ctypes.cast('a', ctypes.c_char_p)

import numpy as np

a = np.array([1,2,3,4,5,6], dtype=np.int32)
print(a)

a = np.array([1.2, 2, 3.1, 4, 5, 6])
print(a)
