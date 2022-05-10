from types import FunctionType
a = (x for x in [1])
print(isinstance(iter(a), Callable))
print(isinstance(iter(a), FunctionType))

# 打印出来的是False，因为generator不能被调用，只能被迭代。
