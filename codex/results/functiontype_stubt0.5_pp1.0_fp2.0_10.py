from types import FunctionType
a = (x for x in [1])
type(a)

# 函数本身也可以赋值给变量，即：变量可以指向函数。
print(type(abs))

# 函数名也是变量
abs = 10

# 可以删除变量
del abs

# 以上代码虽然删除了abs，但是abs()还是可以用
print(abs(-10))

# 变量指向函数后，就可以调用该函数了
a = abs
a(-1)

# 函数名其实就是指向函数的变量
type(a)

# 高阶函
