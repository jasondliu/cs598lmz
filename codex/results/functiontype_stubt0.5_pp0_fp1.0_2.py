from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))

# 判断是否是迭代对象
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))

# 判断是否是生成器
print(isinstance(a, GeneratorType))

# 判断是否是函数
print(isinstance(a, FunctionType))

print(isinstance((x for x in [1]), GeneratorType))
print(isinstance((x for x in [1]), IteratorType))
print(isinstance((x for x in [1]), IterableType))

print(isinstance((x for x in [1]), IteratorType))
print(isinstance((x for x in [1]), IterableType))

print(isinstance((x for x in
