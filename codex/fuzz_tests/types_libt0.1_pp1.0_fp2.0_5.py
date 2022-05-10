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
# a = A()
# print(a.name)
# print(a.age)

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
#         return object.__getattr__
