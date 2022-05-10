import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattr__(self, item):
#         print('__getattr__')
#         return 'A'
#
#     def __getattribute__(self, item):
#         print('__getattribute__')
#         return 'A'
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
#         print('__get__')
#         return 'A'
#
#     def __set__(self, instance, value):
#         print('__set__')
#         instance.__dict__[
