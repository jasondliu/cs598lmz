from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print(f)
print(type(f))
print(type(f) == GeneratorType)
print(type(f) == FunctionType)

for i in f:
    print(i)

# 在调用generator函数时，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从
