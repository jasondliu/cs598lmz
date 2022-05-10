from types import FunctionType
a = (x for x in [1])
type(a)

a = [1,2,3]
type(a)

def fun():
    pass
type(fun)

b = FunctionType
type(b)

# instance 的__class__属性指向它的类
print(a.__class__)

# 类的__bases__属性包含它的所有父类
print(a.__class__.__bases__)

# type的__bases__属性包含它的所有父类
print(type.__bases__)

# object的__class__属性指向它的类
print(object.__class__)

# type的__class__属性指向它的类
print(type.__class__)

# 类的__class__属性指向
