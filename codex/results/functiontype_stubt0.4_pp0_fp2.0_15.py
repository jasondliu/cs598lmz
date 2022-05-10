from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(type(FunctionType))

# 使用isinstance()判断一个对象是否是函数
print(isinstance(print, FunctionType))
print(isinstance(a, FunctionType))

# 使用dir()获取一个对象的所有属性和方法
print(dir(a))
print(dir(print))

# 使用getattr()、setattr()以及hasattr()获取、设置或判断一个对象的属性
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'
