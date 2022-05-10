from types import FunctionType
list(FunctionType(lambda x: x + 1, globals())(1))

# 关键字参数
def f(a, b, c):
    return a + b + c

f(1, 2, 3)
f(1, c=3, b=2)

# 可变参数
def f(*args):
    print(args)

f(1, 2, 3, 4)

# 关键字可变参数
def f(**kwargs):
    print(kwargs)

f(a=1, b=2, c=3)

# 命名关键字参数
def f(*, a, b, c):
    print(a, b, c)

f(a=1, b=2, c=3)

# 参数组合
def f(a, b, c=0, *args, **kwargs):
    print(a, b, c, args,
