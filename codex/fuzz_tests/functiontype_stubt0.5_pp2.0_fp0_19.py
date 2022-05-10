from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>
print(isinstance(a, GeneratorType))
# True
print(isinstance(a, FunctionType))
# False

# 方法2
print(issubclass(GeneratorType, FunctionType))
# True
print(issubclass(GeneratorType, IteratorType))
# True

# 方法3
print(isinstance(a, IteratorType))
# True

print(isinstance(a, IteratorType) and isinstance(a, FunctionType))
# False

print(isinstance(a, IteratorType) or isinstance(a, FunctionType))
# True

print(isinstance(a, IteratorType) and isinstance(a, GeneratorType))
# True
