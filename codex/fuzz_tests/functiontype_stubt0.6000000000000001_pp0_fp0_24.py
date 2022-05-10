from types import FunctionType
a = (x for x in [1])

print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(dir(a))

f = lambda x: x + 1
print(f(2))
print(f(3))

print(type(f))
print(isinstance(f, FunctionType))
print(dir(f))

# generator
def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a + b

for n in fib():
    if n > 100:
        break
    print(n)

print(fib())
print(type(fib()))
print(isinstance(fib(), GeneratorType))
print(isinstance(fib(), FunctionType))
print(dir(fib()))

# 数据类型
a = 10
print(type(a))
print(isinstance(a, int))
print(isinstance(a, str))
print(dir(a))

