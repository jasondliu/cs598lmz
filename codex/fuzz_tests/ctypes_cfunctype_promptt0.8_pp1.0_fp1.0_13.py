import ctypes
# Test ctypes.CFUNCTYPE
func = CFUNCTYPE(c_int, c_int)(add)
print(func(3, 4))
print(func(5, 6))
print(add(7, 8))
print(CFUNCTYPE(c_int, c_int)(add)(9, 10))

# Test ctypes.WINFUNCTYPE
WinFunc = WINFUNCTYPE(c_int, c_int, c_int)(add)
print(WinFunc(5,6))
print(add(7,8))
print(WINFUNCTYPE(c_int, c_int, c_int)(add)(9,10))

# Test ctypes.PYFUNCTYPE
PyFunc = PYFUNCTYPE(c_int, c_int, c_int)(add)
print(PyFunc(5,6))
print(add(7,8))
print(PYFUNCTYPE(c_int, c_int, c_int)(add)(9,10))

# Test ctypes.PYFUNCTYPE with another
