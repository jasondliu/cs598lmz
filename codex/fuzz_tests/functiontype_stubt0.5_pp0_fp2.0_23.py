from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a) is type(b))
print(type(a) is GeneratorType)
print(type(a) is FunctionType)

def gen():
    yield 1

c = gen()
print(type(c) is GeneratorType)
print(type(c) is FunctionType)

# 判断是否是可调用对象
print(callable(gen))
print(callable(b))
print(callable(a))

# 判断是否是模块
import sys
print(type(sys) is ModuleType)

# 判断是否是类
print(type(gen) is ClassType)

# 判断是否是类型
print(type(int) is TypeType)
print(type(type) is TypeType)

# 判断是否是布尔值

