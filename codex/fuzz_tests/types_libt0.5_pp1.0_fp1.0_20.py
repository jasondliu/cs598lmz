import types
types.FunctionType

# 判断一个对象是否是函数
def fn():
    pass

print(type(fn) == types.FunctionType)

# 判断一个对象是否是lambda表达式
print(type(lambda x:x) == types.LambdaType)

# 判断一个对象是否是生成器函数
print(type((x for x in range(10))) == types.GeneratorType)

# 判断一个对象是否是迭代器
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 判断一个对象是否是可迭代对象
from
