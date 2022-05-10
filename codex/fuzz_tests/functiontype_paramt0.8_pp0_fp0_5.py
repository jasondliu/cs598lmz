from types import FunctionType
list(FunctionType(func,globals()) for func in [sum,min])

# 使用闭包
print('-------使用闭包------------')
print('-------函数属性--------')
def func():
    pass
func.__doc__
def func(a,b):
    return a+b
func.__code__.co_varnames
func.__code__.co_argcount

# 在一个外嵌函数里使用外层函数的变量，这个外层函数定义完后就立即执行了
print('-------嵌套函数--------')
def outer():
    x = 1
    def inner():
        print(x)
    inner()
outer()
# 在嵌套函数里对外部函数的变量进行修
