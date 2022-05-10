from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))
# [None]

# 可以通过给函数的__code__属性赋值来改变函数的行为
def add(x, y):
    return x + y

add.__code__ = add.__code__.replace(b'+', b'*')
add(2, 3)
# 6

# 可以通过给函数的__defaults__属性赋值来改变函数的默认参数
def add(x, y=2):
    return x + y

add.__defaults__ = (3,)
add(2)
# 5

# 可以通过给函数的__globals__属性赋值来改变函数的
