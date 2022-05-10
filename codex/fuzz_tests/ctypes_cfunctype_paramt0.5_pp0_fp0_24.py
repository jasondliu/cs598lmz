import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)

def my_callback(a, b, c):
    print(a, b, c)

my_callback_c = FUNTYPE(my_callback)

mylib = ctypes.cdll.LoadLibrary('./mylib.so')
mylib.set_callback(my_callback_c)
mylib.run_callback(1, 2, b'hello')

# 3.2
# https://docs.python.org/3/library/ctypes.html#storing-python-objects-in-ctypes-arrays
# https://stackoverflow.com/questions/12930078/how-to-pass-a-python-list-to-a-c-function-expected-a-ctypes-array-as-an-argume
# https://stackoverflow.com/questions/26114822/python-ctypes-passing-array-of-structs-to-c
# https://stackoverflow.com/questions/
