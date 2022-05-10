from types import FunctionType
a = (x for x in [1])
print(type(a))
# print(a)

# 生成器函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

# 判断是否是生成器函数
print(isinstance(fib(10), GeneratorType))

# 调用生成器函数返回的是一个生成器对象
g = fib(10)
print(type(g))
# print(g)

# 获取生成器的返回值
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 执行
