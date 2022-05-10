from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 判断是否是可调用对象
print(callable(a))
print(callable(a.__next__))

# 判断是否是生成器
print(isinstance(a, GeneratorType))

# 判断是否是迭代器
print(isinstance(a, Iterator))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))

# 判断是否是可迭代对
