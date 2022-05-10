from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

# 判断是否是可调用对象
print(callable(a))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
