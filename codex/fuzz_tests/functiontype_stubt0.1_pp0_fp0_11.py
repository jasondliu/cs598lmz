from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 判断是否是可调用对象
print(callable(a))
print(callable(a.__next__))
print(callable(a.__next__) == True)

# 判断是否是可迭代对象
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(a, Iterator) == True)

# 判断是否是生成器
print(isinstance(a, Generator))
print(isinstance(a, Generator) == True)

# 判断是否是生成器函数
print(isinstance(a, GeneratorFunction))
print(isinstance(a, GeneratorFunction) == True)

# 判断是否是生成
