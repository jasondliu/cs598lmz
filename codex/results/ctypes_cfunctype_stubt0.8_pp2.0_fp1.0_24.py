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

print(json.dumps(b))
# print(b.__dict__)
# print(b.__class__.__dict__)
# print(b.__class__.__bases__)

#
# class C(object):
#     __slots__ = ['a']
#     def __init__(self):
#         self.a = "a"
#
# c = C()
# print(c.__dict__)
# print(c.__class__.__dict__)

import logging

# logging.basicConfig(level=logging.INFO)

