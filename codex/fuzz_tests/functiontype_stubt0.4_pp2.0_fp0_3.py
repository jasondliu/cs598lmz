from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 实现一个生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(6)
print(f)
print(type(f))
print(isinstance(f, GeneratorType))
print(isinstance(f, FunctionType))

for x in f:
    print(x)

print('---------------------------------')

# 调用生成器函数，返回的也是一个生成器对象
g = fib(6)
while True:
    try:
        x = next(g)

