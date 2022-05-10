from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f'))

# 使用lambda表达式创建匿名函数
f = lambda x: x + 1
f(1)

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x + 1
f
f(1)

# 同样可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

f = build(1, 2)
f()

# 匿名函数也是一个函数对
