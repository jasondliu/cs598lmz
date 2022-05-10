import ctypes
ctypes.cast(a, ctypes.c_void_p).value

# -1

ctypes.cast(a, ctypes.c_void_p).value == id(a)

# True

# Python 3
import ctypes
ctypes.cast(a, ctypes.c_void_p).value

# 140809895476760

ctypes.cast(a, ctypes.c_void_p).value == id(a)

# True

# Python 2
import ctypes
ctypes.cast(a, ctypes.c_void_p).value

# -1

ctypes.cast(a, ctypes.c_void_p).value == id(a)

# True
</code>

