import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)
#
# Define the callback type.
#
CALLBACK = FUNTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)

#
# Define the C callback functions.
#
@CALLBACK
def my_callback_func(p1, p2):
    """
    C callback function.
    """
    print('  Python: my_callback_func called with:', p1, p2)
    return 0

@CALLBACK
def my_callback_func_2(p1, p2):
    """
    C callback function.
    """
    print('  Python: my_callback_func_2 called with:', p1, p2)
    return 0

#
# Define the C functions.
#
libc = ctypes.CDLL('libc.so.6')
libc.printf("Hello %s!\n", "World")

#
# Call the C functions.
