import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print("callback(%d, %d)" % (x, y))
    return x + y

def main():
    callback_func = FUNTYPE(callback)
    callback_func(2, 3)

if __name__ == "__main__":
    main()
