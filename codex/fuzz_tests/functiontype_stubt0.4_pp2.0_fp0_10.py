from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))

def gen():
    yield 1
    yield 2
    yield 3

print(gen)
print(type(gen))
print(isinstance(gen, FunctionType))

g = gen()
print(g)
print(type(g))
print(isinstance(g, GeneratorType))

print(next(g))
print(next(g))
print(next(g))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib(10)
print(f)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print
