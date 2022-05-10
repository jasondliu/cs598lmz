from types import FunctionType
a = (x for x in [1])

print(isinstance(a, GeneratorType))

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

f = fib()
print(isinstance(f, GeneratorType))


print(isinstance(fib, FunctionType))
print(isinstance(fib(), GeneratorType))
print(isinstance(f, GeneratorType))

print('f.__name__:', f.__name__)
print('fib.__name__:', fib.__name__)

print(isinstance(fib(), GeneratorType))
print(isinstance(fib, FunctionType))
print(isinstance(fib, GeneratorType))
print(isinstance(fib(), FunctionType))
print(isinstance(fib, FunctionType))

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

print(isinstance(yrange, FunctionType))
print(isinstance(yrange, GeneratorType))
print(isinstance(yr
