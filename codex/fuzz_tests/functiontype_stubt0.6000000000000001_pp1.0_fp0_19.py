from types import FunctionType
a = (x for x in [1])
print(type(a))

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = (x for x in [1])
print(next(a))
print(next(b))

print(list(a))
print(list(b))

print(id(a) == id(b))

# 可以看出每次调用生成器都会生成新的生成器，而且生成器的id是不一样的，说明生成器的每次调用都是一个新的对象

# 测试列表推导式和生成器表达式的区别
import sys

a = [i for i in range(100)]
print(sys.getsizeof(a
