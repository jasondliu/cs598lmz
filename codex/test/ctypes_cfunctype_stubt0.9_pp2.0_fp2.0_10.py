import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    try:
        return [1]
    except ValueError:
        return 'error'

class A(object):
    def __init__(self, func):
        self.func = func
    def __del__(self):
        self.func()

a = A(fun) # segmentation fault

print("ARRIVED HERE")
