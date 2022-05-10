import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'A(%s)' % self.name
#
#     def __repr__(self):
#         return 'A(%s)' % self.name
#
#     def __getattr__(self, item):
#         print('__getattr__', item)
#         return '__getattr__'
#
#     def __getattribute__(self, item):
#         print('__getattribute__', item)
#         return '__getattribute__'
#
#     def __setattr__(self, key, value):
#         print('__setattr__', key, value)
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         print('__delattr__', item)
#         del self.__dict__
