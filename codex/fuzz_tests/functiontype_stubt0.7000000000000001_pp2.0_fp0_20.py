from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [1, 2]
print(type(b))
c = type(FunctionType)
print(c)
d = FunctionType
print(type(d))
# print(type(c))

# 全局变量和局部变量
# 全局变量是在函数外定义的变量，局部变量是在函数内部定义的变量。
# 全局变量的作用域是整个程序，而局部变量的作用域是函数内部。
# 因为局部变量的作用域是函数内部，所以一般情况下命名
