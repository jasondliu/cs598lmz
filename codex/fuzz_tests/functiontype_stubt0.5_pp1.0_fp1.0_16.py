from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

b = (x for x in [1])
print(b)

def gen():
    yield 1

c = gen()
print(c)
print(isinstance(c, FunctionType))
print(isinstance(c, GeneratorType))


def gen_new():
    return 1

print(gen_new())

def gen_new1():
    yield 1

print(gen_new1())

# 基于生成器的协程
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e
