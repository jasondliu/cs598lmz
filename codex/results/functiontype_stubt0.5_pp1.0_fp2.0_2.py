from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))  # True
print(isinstance(a, IteratorType))  # True
print(isinstance(a, IterableType))  # True
print(isinstance(a, FunctionType))  # False
print(isinstance(a, (IteratorType, IterableType, FunctionType)))  # True
print(isinstance(a, (IteratorType, IterableType, FunctionType, dict)))  # False

# 迭代器是否可以被迭代
print(isinstance(a, IteratorType))  # True
print(isinstance(a, IterableType))  # True
print(isinstance(a, FunctionType))  # False
print(isinstance(a, (IteratorType, IterableType, FunctionType)))  # True
print(isinstance(a, (IteratorType, IterableType, FunctionType, dict)))  # False

# 生成器是否可以被迭代
print(isinstance(a, GeneratorType))  # True
