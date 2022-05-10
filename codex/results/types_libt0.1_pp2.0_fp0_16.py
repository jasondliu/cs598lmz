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
# a = A()
# print(a.name)
# print(a.age)

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
# a = A()
# print(a.name)
# print
