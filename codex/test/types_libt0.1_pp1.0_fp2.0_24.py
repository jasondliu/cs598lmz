import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattribute__(self, item):
#         print('__getattribute__')
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         print('__getattr__')
#         return object.__getattr__(self, item)
#
#     def __setattr__(self, key, value):
#         print('__setattr__')
#         return object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         print('__delattr__')
#         return object.__delattr__(self, item)
#
#
# a = A()
# print(a.name)
# a.name = 'B'
