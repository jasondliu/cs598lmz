from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]

# isinstance 检查类型
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

# 使用next遍历generator
# print(next(a))
# print(next(a))

# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"

f = fib(10)
for i in f:
    print(i)

# 判断是否是generator
print(isinstance(fib(10), GeneratorType))
print(isinstance(fib(10), FunctionType))
print(isinstance(f, GeneratorType))
print(isinstance(f, FunctionType))
