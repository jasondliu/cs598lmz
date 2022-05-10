import ctypes
ctypes.cast(0, ctypes.py_object)

# imports for array module
from numpy import array

# create array
array_1 = array([1, 2, 3])
print(array_1)

# create array
array_2 = array([[1, 2, 3], [4, 5, 6]])
print(array_2)

# create array
array_3 = array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(array_3)

# create array
array_4 = array([1, 2, 3], ndmin=5)
print(array_4)

# create array
array_5 = array([1, 2, 3], dtype=complex)
print(array_5)

# create array
array_6 = array([1, 2, 3], dtype=int)
print(array_6)

# create array
array_7 = array([1, 2, 3], dtype=float)
print(array_7)

# create
