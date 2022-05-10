import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattr__(self, item):
#         print('__getattr__')
#         return self.name
#
#     def __getattribute__(self, item):
#         print('__getattribute__')
#         return self.name
#
#     def __setattr__(self, key, value):
#         print('__setattr__')
#         self.name = value
#
#     def __delattr__(self, item):
#         print('__delattr__')
#         del self.name
#
#     def __call__(self, *args, **kwargs):
#         print('__call__')
#         return self.name
#
#     def __str__(self):
#         print('__str__')
#         return self.name
#
#     def __repr__(self):
#
