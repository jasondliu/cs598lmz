import ctypes
ctypes.cast(6, ctypes.py_object)
#Out[18]: 6
ctypes.cast(id(6), ctypes.c_void_p).value
#Out[19]: 94517427755000
id(6)
#Out[20]: 94517427755000
id(ctypes.cast(id(6), ctypes.c_void_p).value)
#Out[21]: 94517427755000
id(ctypes.cast(id(6), ctypes.c_void_p).value) == id(6)
#Out[22]: True
ctypes.cast(id(6), ctypes.c_void_p).value == id(6)
#Out[23]: True
ctypes.cast(id(6), ctypes.c_void_p).value == 94517427755000
#Out[24]: True
ctypes.cast(id(6), ctypes.c_void_p).value
#Out[25]: 94517427755000
ctypes.cast(id(6), ctypes.c_void_p)._type_
