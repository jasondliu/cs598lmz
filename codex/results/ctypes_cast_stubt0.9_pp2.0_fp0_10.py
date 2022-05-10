import ctypes
ctypes.cast(pointer, type)

pointer:指针类型
type: 转化成的目标类型
'''

import ctypes

ll = ctypes.cdll.LoadLibrary
lib = ll("./timestwo.so")
lib.timestwo.restype = ctypes.c_float
lib.timestwo.argtypes = (ctypes.c_float,)

print(lib.timestwo(2.0))
