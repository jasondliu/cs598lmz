from types import FunctionType
a = (x for x in [1])
type(a)

# 判断一个对象是否是函数
print(isinstance(abs, FunctionType))
# 可以直接调用abs()
print(abs(-10))

# 一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-10, 10, abs))

# map()函数接收两个参数，一个是函数，一个是Iterable，
# 将传入的函数依次作用到序列的每个元素，
