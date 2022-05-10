from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 判断一个对象是否是可调用对象
print(callable(a))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
