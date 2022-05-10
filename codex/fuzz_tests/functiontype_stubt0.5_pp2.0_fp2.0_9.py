from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

# 1. generator
# 2. iterator
# 3. iterable

for x in a:
    print(x)

print(next(a))

# for x in a:
#     print(x)

a = iter([1, 2, 3])
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

a = iter([1, 2, 3])
print(a.__next__())
print(a.__next__())
print(a.__next__())
# print(a.__next__())

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b
