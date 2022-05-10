import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self):
#         self.__name = 'A'
#
#     def get_name(self):
#         return self.__name
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.__name = 'B'
#
#
# b = B()
# print(b.get_name())
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.__name = 'C'
#
#
# c = C()
# print(c.get_name())
#
#
# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         self.__name = 'D'
#
#
# d = D()
# print(d.get_name())

#
