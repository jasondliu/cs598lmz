import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self):
#         self.name = 'A'
#
#     def __str__(self):
#         return self.name
#
#
# class B(A):
#     def __init__(self):
#         self.name = 'B'
#
#
# b = B()
# print(b)
#
#
# class C(A):
#     def __init__(self):
#         self.name = 'C'
#
#
# c = C()
# print(c)
#
#
# class D(B, C):
#     def __init__(self):
#         self.name = 'D'
#
#
# d = D()
# print(d)
#
#
# class E(C, B):
#     def __init__(self):
#         self.name = 'E'
#
#
# e = E()
# print(
