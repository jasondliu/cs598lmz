from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IterableType))


# 模拟生成器
def my_range(stop, start = 0, step = 1):
    i = start
    while i < stop:
        yield i
        i += step

# 用生成器模拟map函数
def my_map(func, iter):
    for i in iter:
        yield func(i)

print(type(my_range(10)))
print(type(my_map(lambda x: x, my_range(10))))

# 生成器不能改变元素
a = (i for i in range(10))
print(a.__next__())
print(a.__next__())
# a.remove(2)
# a.remove(3)
print(a.__next__
