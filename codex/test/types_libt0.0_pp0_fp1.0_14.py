import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattr__(self, item):
#         print('__getattr__')
#         return self.name
#
#     def __getattribute__(self, item):
#         print('__getattribute__')
#         return object.__getattribute__(self, item)
#
#
# a = A()
# print(a.name)
# print(a.name)
# print(a.name)
