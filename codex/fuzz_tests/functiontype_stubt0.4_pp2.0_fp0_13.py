from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(next))
print(type(FunctionType))

# 生成器函数

def gen_func():
    yield 1
    yield 2
    yield 3
    return 'haha'

for value in gen_func():
    print(value)

gen = gen_func()
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))

# 生成器表达式

gen = (x for x in range(10))
for value in gen:
    print(value)

# 作业
# 斐波那契数列

def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

def fib(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
       
