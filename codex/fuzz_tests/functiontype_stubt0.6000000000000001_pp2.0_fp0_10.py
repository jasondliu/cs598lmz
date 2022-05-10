from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, FunctionType))
print(dir(a))
print(next(a))

# generator
# 只有在调用时才会生成相应的数据
g = (x * x for x in range(10))
for n in g:
    print(n)

# 函数实现 generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 函数实现 generator
def fib_g(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib_g
