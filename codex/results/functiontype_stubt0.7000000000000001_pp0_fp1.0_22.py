from types import FunctionType
a = (x for x in [1])
print(a)
b = (x for x in [2])
print(b)
print(a.__class__)
print(isinstance(a, GeneratorType))
print(a == b)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib_gen = fib(6)
print(fib_gen.__class__)
print(isinstance(fib_gen, GeneratorType))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
# print(next(fib_gen))

for n in fib(6):
    print(n)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:
