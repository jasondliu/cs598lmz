from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# 使用lambda表达式可以简化函数定义，但是不能访问函数内的变量

# 匿名函数可以作为返回值
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)

# 匿名函数也可以作为参数传递
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

# 可以使用匿名函数过滤列表
# 这里的匿
