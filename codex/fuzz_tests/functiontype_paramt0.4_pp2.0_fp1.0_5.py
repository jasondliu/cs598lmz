from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# 元组
t = (1, 2, 3, 4, 5)
# 注意，tuple() 函数可以将列表转换成元组
tuple(t)

# 字典
d = {'a': 1, 'b': 2, 'c': 3}
# 注意，dict() 函数可以将元组转换成字典
dict(d)

# 集合
s = {1, 2, 3, 4, 5}
# 注意，set() 函数可以将列表转换成集合
set(s)

# 冻结集合
frozens
