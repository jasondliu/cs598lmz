import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattribute__(self, item):
#         print('__getattribute__', item)
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         print('__getattr__', item)
#         return '__getattr__'
#
#     def __setattr__(self, key, value):
#         print('__setattr__', key, value)
#         return object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         print('__delattr__', item)
#         return object.__delattr__(self, item)
#
# a = A()
# print(a.name)
# print(a.age)
# a.age = 18
# del a.age

#
