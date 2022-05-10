import types
types.MethodType(lambda self, x: x, object())

# TypeError: can't set attributes of built-in/extension type 'object'

# 可以给一个实例绑定一个方法，该实例调用这个方法时，会把自己作为第一个参数传入

# 给实例绑定的方法，对另一个实例是不起作用的

# 给一个实例绑定的方法，对另一个实例是不起作用的：

class Student(object):
    pass

s = Student()
s.name = 'Michael'

def set_age(self, age):
    self.age = age


