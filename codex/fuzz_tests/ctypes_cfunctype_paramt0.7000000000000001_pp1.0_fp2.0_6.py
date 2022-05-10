import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def call_func(func, arg):
    func(arg)

if __name__ == '__main__':
    my_func = FUNTYPE(lambda x: x+1)
    call_func(my_func, 1)
</code>

