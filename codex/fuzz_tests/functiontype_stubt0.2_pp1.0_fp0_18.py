from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

# 判断一个对象是否是函数
def fn():
    pass

print(isinstance(fn, FunctionType))
print(isinstance(fn, types.FunctionType))

# 判断一个对象是否是生成器
print(isinstance(a, types.GeneratorType))

# 判断一个对象是否是迭代器
print(isinstance([], Iterator))
print(isinstance((x for x in []), Iterator))

# 判断一个对象是否是可迭代对象
print(isinstance([], Iterable))
print(isinstance((x for x in []), Iterable))

#
