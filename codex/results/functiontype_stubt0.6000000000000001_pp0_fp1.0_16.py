from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
# print(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

def func():
    pass

print(type(func))
print(type(a) == type(func))
print(type(a) == FunctionType)

print(isinstance(a, FunctionType))
print(isinstance(func, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(func, GeneratorType))

# 总结
# 函数和生成器不同之处在于，函数可以被多次调用，而生成器只能迭代一次。
# 函数返回多个值，而生成器返回单个值。
