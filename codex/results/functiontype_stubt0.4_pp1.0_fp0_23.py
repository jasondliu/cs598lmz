from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x:x))

# 判断对象是否可调用
print(callable(a))
print(callable(lambda x:x))
print(callable(FunctionType))

# 判断对象是否可迭代
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance("abc", Iterator))
print(isinstance("abc", Iterable))

# 判断对象是否可以进行切片
print(isinstance(a, slice))
print(isinstance("abc", slice))
print(isinstance([1,2,3], slice))
print(isinstance(range(10), slice))

# 判断对象是否可以进行索引
print(isinstance(a, int))
print(isinstance("abc", int
