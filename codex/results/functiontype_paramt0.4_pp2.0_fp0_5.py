from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# 利用生成器表达式创建列表
L = [x * x for x in range(10)]
L
# 利用生成器表达式创建生成器
g = (x * x for x in range(10))
g

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 将fib函数变成生成器
def fib_gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
       
