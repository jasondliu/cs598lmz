import ctypes
ctypes.cast(0, ctypes.py_object).value

# from ctypes import cdll # load cdll
# cdll.LoadLibrary("./test.so") # load .so
# lib = CDLL("./test.so") # load .so
# lib.func() # call func

import ctypes
lib = ctypes.cdll.LoadLibrary('./libtest.so')
r = lib.func()
print(r)

# python 3.2
# import ctypes
# lib = ctypes.cdll.LoadLibrary('./libtest.so')
# print(lib.func())

# python 3.3
# import ctypes
# lib = ctypes.CDLL('./libtest.so', ctypes.RTLD_GLOBAL)
# print(lib.func())

# python 3.4
# import ctypes
# lib = ctypes.CDLL('./libtest.so', ctypes.RTLD_GLOBAL)
# print(lib.func())
