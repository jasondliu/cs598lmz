from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(a, type))

# 判断是否是可迭代对象
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 判断是否是迭代器对象
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 判断是否是生成器
print(isinstance((x for x in range(10)),
