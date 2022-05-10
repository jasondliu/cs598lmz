from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print("-" * 50)

def fib(num):
    a, b = 1, 1
    for x in range(num):
        yield a
        a, b = b, a + b


print(type(fib))
print(type(fib(5)))
print(type(fib(5)) == GeneratorType)
print(type(fib(5)) == FunctionType)
