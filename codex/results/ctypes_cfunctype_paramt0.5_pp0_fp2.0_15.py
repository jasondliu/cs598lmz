import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def get_func(lib, name, restype=None, argtypes=[]):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def main():
    lib = ctypes.cdll.LoadLibrary('./lib_test.so')
    my_add = get_func(lib, 'my_add', ctypes.c_int, [ctypes.c_int, ctypes.c_int])
    print(my_add(1, 2))

    my_add_2 = get_func(lib, 'my_add_2', ctypes.c_int, [ctypes.c_int, ctypes.c_int])
    print(my_add_2(1, 2))

    my_add_3 = get_func(lib, 'my_add_3', ctypes.c_int, [ctypes.c_int, ctypes.c_int])

