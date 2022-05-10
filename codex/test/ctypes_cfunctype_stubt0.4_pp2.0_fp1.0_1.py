import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

# print(fun())

# int_array = ctypes.c_int * 3
# print(int_array)
# print(int_array(1, 2, 3))
# print(int_array(1, 2, 3)[1])
# print(int_array(1, 2, 3)[1:])
# print(int_array(1, 2, 3)[1:][0])
# print(int_array(1, 2, 3)[1:][0] == 2)

# print(ctypes.c_int(1))
# print(ctypes.c_int(1).value)
# print(ctypes.c_int(1).value == 1)

# print(ctypes.c_int(1).value == 1)
# print(ctypes.c_int(1).value == 2)
# print(ctypes.c_int(1).value == 3)

# print(ctypes.c_int(1).value == 1)
# print(ctypes.c_int(1).value == 2
