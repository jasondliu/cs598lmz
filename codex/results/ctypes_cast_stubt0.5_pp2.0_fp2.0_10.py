import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is the only way to access the data of an array created by
# array.array:
a = array.array('i', range(3))
# Indexing the array yields an integer
print(a[0])
# use ctypes arrays to get a mutable buffer
import ctypes
b = ctypes.cast(a.buffer_info()[0], ctypes.POINTER(ctypes.c_int))
print(b[0])

# The buffer protocol is supported by array.array, too.
print(a.buffer_info())
print(ctypes.cast(a.buffer_info()[0], ctypes.POINTER(ctypes.c_int)))

# array.array also allows creating an array from a string.
a = array.array('u', 'hello \u2641')
print(a.tounicode())

# The following code reads the contents of a file as an array of bytes.
# It uses the fromfile() class method.
# The optional argument used for fromfile() controls the number of bytes

