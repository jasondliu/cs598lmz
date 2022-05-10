from types import FunctionType
a = (x for x in [1])
b = [1]
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# 判断是否是生成器
print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(b, (GeneratorType, FunctionType)))

# 判断是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

# 判断是否是迭代器
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

# 判断是否是可迭代对象或者迭代器
print(isinstance(a, (Iterable, Iterator)))
print(isinstance(b, (Iterable, Iterator)))

# 判断是
