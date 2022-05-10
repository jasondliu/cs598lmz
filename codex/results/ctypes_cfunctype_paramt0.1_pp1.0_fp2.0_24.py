import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1, 2)

# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
# my_callback_c(1, 2)
