import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 0)
# <CFunctionType object at 0x7f7b38eec948>

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
# <CFunctionType object at 0x7f7b38eec8e0>

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y: x + y)
# <CFunctionType object at 0x7f7b38eec8e0>

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(lambda x, y, z: x + y + z)
# <CFunctionType object at 0x7f7b38eec8e0>


# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c
