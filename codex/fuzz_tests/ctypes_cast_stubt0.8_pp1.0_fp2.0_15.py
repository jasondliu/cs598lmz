import ctypes
ctypes.cast(x, ctypes.py_object).value

# There are also a number of built-in functions that do not create `numpy` arrays.
sum(x)
# Type of output array?
type(sum(x))
# Type of input array?
type(x)
max(x)
# Type of output array?
type(max(x))
# Type of input array?
type(x)
min(x)
# Type of output array?
type(min(x))
# Type of input array?
type(x)

# There are also a number of built-in functions that do not create `numpy` arrays.
np.sum(x)
# Type of output array?
type(np.sum(x))
# Type of input array?
type(x)
np.max(x)
# Type of output array?
type(np.max(x))
# Type of input array?
type(x)
np.min(x)
# Type of output array?
type(np.min(x))
# Type of input array?
type(x)

