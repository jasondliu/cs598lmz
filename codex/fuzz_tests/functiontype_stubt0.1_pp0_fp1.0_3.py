from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 判断是否是可调用对象
print(callable(a))
print(callable(a.__next__))
print(callable(a.__next__) == True)

# 判断是否是生成器
print(isinstance(a, GeneratorType))
print(isinstance(a, GeneratorType) == True)

# 判断是否是生成器函数
def gen():
    yield 1

print(isinstance(gen(), GeneratorType))
print(isinstance(gen(), GeneratorType) == True)

# 判断是否是生成器函数
print(isgeneratorfunction(gen))
print(isgeneratorfunction(gen) == True)

# 判断是否是生成器

