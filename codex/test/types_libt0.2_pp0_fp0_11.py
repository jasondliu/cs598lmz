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
