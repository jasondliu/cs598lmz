from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = (x for x in [1])
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print(a == b)
print(a is b)

# 这里可以看出，生成器是一个特殊的迭代器，它是可迭代对象，但不是迭代器
# 生成器是一个可迭代对象，但不是迭代器
# 生成器是一个迭代器，但不是可迭代对象
# 生成器是一个可迭代对象
