from types import FunctionType
list(FunctionType(lambda: None, globals()).__globals__.keys())

# 定义一个函数
def func():
    pass

# 打印函数的名字
print(func.__name__)

# 打印函数的所有属性
print(dir(func))

# 打印函数的所有属性
print(dir(func))

# 获取函数的所有全局变量
print(func.__globals__)

# 获取函数的所有局部变量
print(func.__code__.co_varnames)

# 获取函数的所有局部变量
print(func.__code__.co_varnames)

# 获取函数的
