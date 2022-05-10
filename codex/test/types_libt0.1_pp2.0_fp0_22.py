import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return self.name
#
#
# class B(A):
