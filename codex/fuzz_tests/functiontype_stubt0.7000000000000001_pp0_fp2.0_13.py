from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 生成器
a = (x for x in [1])
print(a)
print(a.__next__())

# 多层生成器
a = ((x, y) for x in [1, 2, 3] for y in [1, 2, 3])
print(a)
print(a.__next__())

# 斐波那契数列
def fib(max):
    i, j, n = 0, 1, 0
    while n < max:
        yield j
        i, j = j, i + j
        n += 1
    return 'done'

a = fib(5)
print(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

#
