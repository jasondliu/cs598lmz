from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# 把函数名当作变量赋值
print(abs)
f = abs
print(f)
print(f(-10))

# 函数名也是变量
abs = 10
print(abs)
# abs(-10)

# 可以把函数名赋给变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-10))

# 函数本身也可以赋值给变量，即：变量可以指向函数
def add(x, y, f):
    return f(x) + f(y)


