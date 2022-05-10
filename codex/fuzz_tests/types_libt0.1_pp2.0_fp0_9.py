import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattr__(self, item):
#         return 'A'
#
#
# class B(A):
#     def __init__(self):
#         self.name = 'B'
#
#     def __getattr__(self, item):
#         return 'B'
#
#
# b = B()
# print(b.name)
# print(b.age)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattribute__(self, item):
#         return 'A'
#
#
# class B(A):
#     def __init__(self):
#         self.name = 'B'
#
#     def __getattribute__(self, item):
#         return 'B'
#

