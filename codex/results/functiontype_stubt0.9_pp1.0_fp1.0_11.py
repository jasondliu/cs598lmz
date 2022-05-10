from types import FunctionType
a = (x for x in [1])
isinstance(a['__iter__'], FunctionType)

print(isinstance.__doc__)

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(abs))
print(len("ABCDEFGH"))
print("ABCDEFGH".__len__())

# 利用setattr()可以动态给属性赋值
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(hasattr(obj, 'x')) # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(getattr(obj, 'y
