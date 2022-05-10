import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)



def my_func(x):
    # this happens in C  space
    x += 42
    print('my_func', x)


my_func_c_bound_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_func)

if __name__ == "__main__":
    print(my_func_c_bound_func)
    b = BoundFunc()
  
