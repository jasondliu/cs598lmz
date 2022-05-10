from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['x', 'y']

# 一个简单的函数
def func(x, y):
    return x + y

# 函数的名称
print(func.__name__)

# 函数的文档字符串
print(func.__doc__)

# 函数的全局名称空间
print(func.__globals__)

# 函数的参数列表
print(func.__code__.co_varnames)

# 函数的默认参数值
print(func.__defaults__)

# 函数的关键字参数值
print(func.__kwdefaults__)

# 函数的闭包
