from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

# 函数
def f1():
    pass
print(f1)
print(type(f1))
print(type(FunctionType))

# 模块
import sys
print(sys)
print(type(sys))

# 类
class C:
    pass
c = C()
print(c)
print(type(c))

# 实例
print(type(c)())

# 类型
print(type(type))

# 元类
print(type(type))

# 对象
o = object()
print(o)
print(type(o))
