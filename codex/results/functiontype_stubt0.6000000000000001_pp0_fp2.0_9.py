from types import FunctionType
a = (x for x in [1])
b = list(a)
print(b)

a = (x for x in range(10))
b = list(a)
print(b)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))


def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


print(fib(10))
print(isinstance(fib(10), GeneratorType))
print(isinstance(fib(10), FunctionType))

print(list(fib(10)))


def fib_generator(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


fib = fib_generator(10)
print(fib)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print
