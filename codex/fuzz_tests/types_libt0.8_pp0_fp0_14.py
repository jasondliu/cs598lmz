import types
types.MethodType(func, None, class1)
class1.method()

'''
对实例方法的调用被转换为：

类名称.实例方法名称（第一个参数，self，可以被省略）
'''

#给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
class1.set_age = MethodType(set_age, class1)
class1.set_age(25)
#给一个实例绑定的方法，对另一个实例不起作用，只对当前实例起作用
class2
