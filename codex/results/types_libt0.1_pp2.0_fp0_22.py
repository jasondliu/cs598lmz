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
#     def __init__(self):
#         self.name = 'B'
#
#
# class C(A):
#     def __init__(self):
#         self.name = 'C'
#
#
# class D(B, C):
#     def __init__(self):
#         self.name = 'D'
#
#
# d = D()
# print(d)
# print(d.__class__.__name__)
# print(d.__class__.__mro__)
# print(d.__class__.__bases__)
# print(d.__class__.__dict__
