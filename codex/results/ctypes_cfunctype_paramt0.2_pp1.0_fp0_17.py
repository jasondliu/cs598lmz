import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_type = FUNTYPE(my_callback)

my_callback_type(1, 2)

my_callback_type(3, 4)

my_callback_type(5, 6)

my_callback_type(7, 8)

my_callback_type(9, 10)

my_callback_type(11, 12)

my_callback_type(13, 14)

my_callback_type(15, 16)

my_callback_type(17, 18)

my_callback_type(19, 20)

my_callback_type(21, 22)

my_callback_type(23, 24)

my_callback_type(25, 26)

my_callback_type(27, 28)

my_callback_type(29, 30)

