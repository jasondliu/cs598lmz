from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import array
a = array.array('i', range(5))
a

import numpy as np
np.array([1, 4, 2, 5, 3])

np.array([3.14, 4, 2, 3])

np.array([1, 2, 3, 4], dtype='float32')

# nested lists result in multi-dimensional arrays
np.array([range(i, i + 3) for i in [2, 4, 6]])

# Create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)

# Create a 3x5 floating-point array filled with ones
np.ones((3, 5), dtype=float)

# Create a 3x5 array filled with 3.14
np.full((3, 5), 3.14)

# Create an array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2
# (this is similar to the built-in range() function)
np.arange
