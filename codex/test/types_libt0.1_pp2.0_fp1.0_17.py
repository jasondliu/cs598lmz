import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self):
#         self.name = 'A'
#
#     def __getattr__(self, item):
#         return 'A'
#
#
# class B(A):
