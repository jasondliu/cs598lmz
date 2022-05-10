import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self):
#         self.name = 'A'
#
#     def __str__(self):
#         return self.name
#
#
# class B(A):
#     def __init__(self):
#         super(B, self).__init__()
#         self.name = 'B'
#
#
# class C(A):
#     def __init__(self):
#         super(C, self).__init__()
#         self.name = 'C'
#
#
# class D(B, C):
#     def __init__(self):
#         super(D, self).__init__()
#         self.name = 'D'
#
#
# d = D()
# print(d)
# print(D.__mro__)

# class A(object):
#     def __init__(self):
#         self.name = 'A
