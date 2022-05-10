from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

# 判断是否是某种类型
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

# 判断是否是某种类型
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

# 判断是否是某种类型
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

# 判断是否是某种类型
print(isinstance(a, Iterator))
print
