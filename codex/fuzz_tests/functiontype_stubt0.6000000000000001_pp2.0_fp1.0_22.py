from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

# 函数
def f(x):
    return x*x

print(f)
print(type(f))

# 模块
import sys
print(sys)
print(type(sys))

# 类
class A:
    pass

print(A)
print(type(A))

# 方法
a = A()
print(a)
print(type(a))

# 类型
print(type(type))
