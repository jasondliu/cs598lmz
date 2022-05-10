import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b, c):
    print("a:", a, "b:", b, "c:", c)
    return a + b + c

def my_callback_2(a, b, c):
    print("a:", a, "b:", b, "c:", c)
    return a + b + c

def my_callback_3(a, b, c):
    print("a:", a, "b:", b, "c:", c)
    return a + b + c

def my_callback_4(a, b, c):
    print("a:", a, "b:", b, "c:", c)
    return a + b + c

def my_callback_5(a, b, c):
    print("a:", a, "b:", b, "c:", c)
    return a + b + c

def my_callback_6(
