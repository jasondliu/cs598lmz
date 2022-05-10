from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

# 判断一个对象是否是函数
print(callable(a))
print(callable(a.__next__))
print(callable(a.__next__) == True)

# 判断一个对象是否是某种类型
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))
print(isinstance(a, types.FunctionType) == False)

# 判断一个对象是否是某种类型
print(issubclass(type(a), types.GeneratorType))
print(issubclass(type(a), types.FunctionType))
print(issubclass
