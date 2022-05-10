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
#         return '__setattr__'
#
#     def __delattr__(self, item):
#         print('__delattr__')
#         return '__delattr__'
#
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#         return '__call__'
#
#     def __str__(self):
