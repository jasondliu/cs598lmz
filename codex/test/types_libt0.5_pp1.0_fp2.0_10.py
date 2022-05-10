import types
types.MethodType(some_func, None, MyClass)

# 定义一个类
class Student(object):
    pass

# 定义一个实例
bart = Student()

# 给实例绑定一个属性
bart.name = 'Bart Simpson'
print(bart.name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
bart.set_age = MethodType(set_age, bart)
bart.set_age(25)
print(bart.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
bart2 = Student()
# bart2.set_age(25)

# 为了给所有
