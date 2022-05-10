import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = "A"
#
#     def __getattr__(self, item):
#         print("getattr")
#         return self.name
#
#     def __getattribute__(self, item):
#         print("getattribute")
#         return self.name
#
#
# a = A()
# print(a.name)
# print(a.name)
# print(a.name)

# class A(object):
#     def __init__(self):
#         self.name = "A"
#
#     def __getattr__(self, item):
#         print("getattr")
#         return self.name
#
#     def __getattribute__(self, item):
#         print("getattribute")
#         return self.name
#
#
# a = A()
# print(a.name)
# print(a.name
