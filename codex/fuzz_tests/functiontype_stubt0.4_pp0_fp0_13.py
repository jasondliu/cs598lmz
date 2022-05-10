from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(FunctionType))

# 定义一个函数，返回一个生成器对象
def func():
    yield 1
    yield 2
    yield 3
    yield 4

# 打印函数func的类型
print(type(func))

# 定义一个生成器对象
g = func()
print(type(g))

# 打印生成器对象的下一个元素
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# 定义一个生成器函数
def func():
    yield 1
    yield 2
    yield 3
    yield 4

# 定义一个生
