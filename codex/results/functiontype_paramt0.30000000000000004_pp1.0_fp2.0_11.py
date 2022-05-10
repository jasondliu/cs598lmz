from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用lambda表达式创建匿名函数
# lambda表达式创建的函数只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数可以直接赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
f(5)

# 匿名函数也可以作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

# 匿名函数
