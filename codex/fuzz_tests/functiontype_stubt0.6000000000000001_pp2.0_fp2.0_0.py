from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a)
print(b)
print(a is b)
print(type(a) == type(b))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 在python 2.6版本之前，使用types.GeneratorType这个类型判断，在2.6之后，使用collections.Generator
# 在python 3.3之后，types.GeneratorType被移除，只保留了collections.Generator

# 在python 3.3之后，collections.Generator被移除，只保留了types.GeneratorType
# collections.Generator已经不存在了，types.GeneratorType的可以通过isinstance(x
