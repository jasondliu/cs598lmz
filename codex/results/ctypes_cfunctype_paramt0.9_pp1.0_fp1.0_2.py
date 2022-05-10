import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_char_p, ctypes.c_char_p)


@FUNTYPE
def callback1(a, c):
    print(a+c)
    return 0x88


lib.register_callback(1, callback1)


def calback_wrapper(a, c):
    print(a+c)
    print(lib.add(5, 6))
    return 0x77

lib.register_callback(3, calback_wrapper)

lib.callback_check()
# lib.register_callback(15, )
# lib.callback_check()
