import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
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
#         super().__setattr__(key, value)
#
#     def __delattr__(self, item):
#         print('__delattr__')
#         super().__delattr__(item)
#
#     def __get__(self, instance, owner):
#         print('__get__')
#         return '__get__'
#
#     def __set__(self, instance, value):
#         print('__set__')
