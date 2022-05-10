import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world!"

class MyObject(object):
    def __init__(self):
        self.my_attr = 123
        self.my_func = fun

