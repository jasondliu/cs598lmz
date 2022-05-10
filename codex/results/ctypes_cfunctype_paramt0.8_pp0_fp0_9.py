import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
c_func = FUNTYPE(func)


def exec_func():
    print('before func...')
    c_func()
    print('after func...')


exec_func()
