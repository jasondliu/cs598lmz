from types import FunctionType
list(FunctionType())

# TypeError: 'function' object is not iterable

# 测试普通函数
def f():
    pass

list(FunctionType())
