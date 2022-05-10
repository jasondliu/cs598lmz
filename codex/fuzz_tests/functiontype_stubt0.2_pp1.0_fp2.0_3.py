from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == types.FunctionType)

# 判断是否是某种类型可以用isinstance()判断
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

# 判断是否是某种类型可以用isinstance()判断
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

# 判断是否是某种类型可以用isinstance()判断
print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

# 判断是否是
