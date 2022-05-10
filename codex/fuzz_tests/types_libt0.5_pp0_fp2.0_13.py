import types
types.MethodType(func,obj)
obj.func()

# 给实例绑定的方法，对另一个实例是不起作用的

# 给class绑定方法
# 给class绑定方法，可以直接在class中定义函数
class Student(object):
    pass
def set_age(self,age):
    self.age = age
Student.set_age = set_age

s = Student()
s.set_age(25)
s.age

# 使用__slots__
# 只允许对Student实例添加name和age属性
# 定义__slots__ 变量，来限制该class实例能添加的属性
