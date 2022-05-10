from types import FunctionType
list(FunctionType(f1).__code__.co_varnames)

import inspect
from types import FunctionType
print(f1.__code__.co_freevars)
inspect.getclosurevars(f1)

# 变量的作用域
a = 1
def fun():
    # 1. 先在自己的局部作用域中找
    # 2. 再在外部作用域中找
    print(a)
fun()

# 局部作用域引用外部作用域变量,外部作用域对该变量可以做改变
# a = 1
# def fun():
#     a = 2
#     print(a)
# fun()
# print(a)

a = 1
def fun():
    global a
    a = 2
    print(a
