from types import FunctionType
a = (x for x in [1])
print(type(a))
# 迭代器
print(isinstance(a,Iterator))
# 生成器
print(isinstance(a,Generator))
# 可迭代
print(isinstance(a,Iterable))
# 用来判断是不是函数
print(isinstance(a,FunctionType))
# import types
#
# print(type(a))
# print(type(next))
# print(type(type))
# print(type(type(1)))
#
#
# def fn():
#     pass
#
#
# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x: x)==types.LambdaType)
# print(type(x for x in range(10))==types.GeneratorType)


"""
切片
"""
l =[1,2,3,4,5]
s = slice(0,3)
