from types import FunctionType
a = (x for x in [1])
b = lambda : 1
print(isinstance(a, GeneratorType))
print(isinstance(b, FunctionType))

a = (x for x in [1])
b = lambda : 1
print(isinstance(a, Iterator))
print(isinstance(b, Callable))

# 定义一个生成器函数
def fib(max):
    n,a,b = 0,0,1
    while n < max :
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

# for循环调用生成器函数
for x in fib(6):
    print(x)

# 定义一个生成器函数
def fib(max):
    n,a,b = 0,0,1
    while n < max :
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done
