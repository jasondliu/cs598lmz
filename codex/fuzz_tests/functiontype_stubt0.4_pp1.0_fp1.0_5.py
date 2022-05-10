from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.__next__())
print(next(a))

print(a.__next__())

# 不可以迭代的生成器

def my_generator():
    yield 1
    yield 2
    yield 3

for i in my_generator():
    print(i)

print(my_generator())

# 列表推导式

a = [x for x in range(10)]
print(a)

# 生成器表达式

a = (x for x in range(10))
print(a)

for i in a:
    print(i)

print(a.__next__())
print(a.__next__())

# 生成器函数

def my_generator():
    yield 1
    yield 2
    yield 3

a = my_
