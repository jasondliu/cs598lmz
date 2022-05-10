import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"
class A(object):
    pass
print(fun.__dict__)
a = A()
a.agent = fun
print(a.agent.__dict__)
print(a.__dict__)

import json
class B(object):
    def __init__(self):
        self.a = "a"

    def __getitem__(self, item):
        self.item = item
        return item

b = B()

