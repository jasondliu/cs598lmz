from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))

# 生成器函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)
print(type(f))
print(isinstance(f, Iterator))
print(isinstance(f, Iterable))
print(isinstance(f, Generator))
print(isinstance(f, FunctionType))

for x in f:
    print(x)

# 获取返回值
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)

