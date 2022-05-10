from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))


# import types
#
# class A:
#     a = None
#
#     def __init__(self):
#         self.a = 1
#
#     def foo(self):
#         return 1
#
# a = A()
# print(type(a.foo))
# print(isinstance(a.foo, types.MethodType))
#
# print(type(a.foo) is types.MethodType)
# print(type(a.foo) is types.FunctionType)
# print(type(a.foo) is types.BuiltinMethodType)
# print(type(a.foo) is types.BuiltinFunctionType)
#
# print(type(print))
# print('done')
