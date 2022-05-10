from types import FunctionType
a = (x for x in [1])

print(type(lambda a: a))
print(type(a))

class A(object):
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

a1 = A(1)
a2 = A(b = 1)
a3 = A()
print(a1.a, a1.b)
print(a2.a, a2.b)
print(a3.a, a3.b)

# 现在新增一个数据项c，有很多对象，不能单独为每个对象设置，
# 可以用setattr() 或 __setattr__ 来设置
a1 = A(1)
a2 = A(1);
print(getattr(a1,'c'))
# 方法1

