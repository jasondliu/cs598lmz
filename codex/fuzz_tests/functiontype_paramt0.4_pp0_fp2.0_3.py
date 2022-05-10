from types import FunctionType
list(FunctionType(lambda x: x, globals()).__code__.co_varnames)

# 其他方法
def foo():
    a = 1
    b = 2
    c = 3
    return locals()

# 打印出字典
foo()

# 返回字典的key列表
list(foo().keys())

# 返回字典的value列表
list(foo().values())

# 返回字典的key和value列表
list(foo().items())

# 返回字典的key列表
list(foo().keys())

# 返回字典的key列表
list(foo().keys())

# 返回字典的key列表
list(foo().keys())
