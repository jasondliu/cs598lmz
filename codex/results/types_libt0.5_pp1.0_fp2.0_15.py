import types
types.FunctionType

# 判断一个对象是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)

# 判断一个对象是否是lambda表达式
print(type(lambda x: x) == types.LambdaType)

# 判断一个对象是否是生成器函数
print(type(x for x in range(10)) == types.GeneratorType)

# 使用isinstance()判断一个对象是否是Iterable对象
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 使用isinstance()判断
