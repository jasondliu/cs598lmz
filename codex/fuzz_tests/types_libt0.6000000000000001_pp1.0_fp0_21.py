import types
types.MethodType(method, obj)

# 创建一个类
class Dog(object):
    __slots__ = ('walk', 'age', 'name') # 用tuple定义允许绑定的属性名称

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType

d = Dog()
d.set_age = MethodType(set_age, d) # 给实例绑定一个方法
d.set_age(25)
d.age


# 给一个实例绑定的方法，对另一个实例是不起作用的：
d2 = Dog()
d2.set_age(30)

# 为了
