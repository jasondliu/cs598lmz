from types import FunctionType
a = (x for x in [1])
print(a, type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# 生成器函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print(f, type(f))
print(isinstance(f, GeneratorType))
print(isinstance(f, FunctionType))
print(isinstance(f, Iterator))
print(isinstance(f, Iterable))

# 可以通过next()函数获得generator的下一个返回值
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f
