import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattr__(self, item):
#         print('__getattr__')
#         return '__getattr__'
#
#     def __getattribute__(self, item):
#         print('__getattribute__')
#         return '__getattribute__'
#
#     def __setattr__(self, key, value):
#         print('__setattr__')
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         print('__delattr__')
#         del self.__dict__[item]
#
#     def __get__(self, instance, owner):
