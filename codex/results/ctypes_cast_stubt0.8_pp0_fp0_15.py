import ctypes
ctypes.cast(ptr, ctypes.py_object).value

ptr = ctypes.pointer(ctypes.c_int(42))
ctypes.cast(ptr, ctypes.c_char_p).value


int_arr = (ctypes.c_int*10)()
ctypes.cast(int_arr, ctypes.POINTER(ctypes.c_int))


class MyStructure(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_float)]

ptr = ctypes.pointer(MyStructure(1, 2.0))
ctypes.cast(ptr, ctypes.POINTER(MyStructure)).contents


str_arr = ("one", "two", "three")
ctypes.cast(str_arr, ctypes.c_char_p)


class POINTER(ctypes.c_char_p):
    pass

ctypes.cast(str_arr, POINTER)


class POINTER(ctypes.POINTER(ctypes.c_char)):
    pass

