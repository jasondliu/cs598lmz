from _struct import Struct
s = Struct.__new__(Struct)
s.format = '7s'
s.size = s.calcsize(s.format)
print(s.size)

# 使用缺省参数
def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)
x = (1, 2)
spam(x)
spam(*x)

# 在参数前加上*时，后面只能是位置参数
def spam(a, *b):
    print(a, b)

spam(1, 2, 3)

# 在参数前加上**时，后面只能是关键字参数
def spam(a, **b):
    print(a, b)

spam(1, x=2, y=3)

# 在函数内
