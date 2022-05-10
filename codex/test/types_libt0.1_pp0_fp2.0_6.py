import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
