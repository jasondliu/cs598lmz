from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a) == type(b))
print(FunctionType == type(a))
print(type(a) == type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(a is b)
print(a == b)
print(a is not b)
print(a != b)

# 迭代器
# 可迭代对象
a = [1, 2, 3]
b = iter(a)
print(b)
print(next(b))
print(next(b))
print(next(b))
# print(next(b))

# 生成器
def my_gen():
    yield 1
    yield 2
    yield 3

a = my_gen()
print(a)
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

# 协
