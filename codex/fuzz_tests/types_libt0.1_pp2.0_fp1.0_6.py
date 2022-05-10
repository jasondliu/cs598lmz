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
# b = B()
# print(b)

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
#     def __str__(self):
#         return self.name
#
#
# b = B()
# print(b)


