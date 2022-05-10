from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# 利用__code__.co_varnames属性，可以获取函数的参数名称
def func(a, b, c):
    pass

list(func.__code__.co_varnames)

# 利用__code__.co_argcount属性，可以获取函数的参数个数
def func(a, b, c):
    pass

func.__code__.co_argcount

# 利用__code__.co_consts属性，可以获取函数的常量
def func(a, b, c):
    pass

func.__code__.co_consts

# 利用__code__.co_names属性，
