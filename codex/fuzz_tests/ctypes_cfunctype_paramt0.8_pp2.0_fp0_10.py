import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def main():
    lib = ctypes.CDLL('./libfoo.so')
    lib.say_hello()

    callback = FUNTYPE(my_callback)
    lib.register_callback(callback)

    lib.call_registered_callback(2, 3)

def my_callback(x, y):
    print('my_callback', x, y)

if __name__ == '__main__':
    main()
