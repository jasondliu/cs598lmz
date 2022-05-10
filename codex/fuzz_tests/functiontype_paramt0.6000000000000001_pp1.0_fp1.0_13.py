from types import FunctionType
list(FunctionType(lambda x, y: x + y, {})(1, 2))

# 高阶函数
# 变量可以指向函数
f = abs
f
# 函数名也是变量
print(abs(-10))
print(f(-10))

# 函数名也是变量，指向函数对象
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称为高阶函数
def add(x, y, f):
    return f(x) + f
