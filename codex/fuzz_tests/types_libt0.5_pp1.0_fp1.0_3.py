import types
types.MethodType(new, x)
x.method()

# 给实例绑定属性
x.name = 'x'
print(x.name)

# 给实例绑定方法
def setName(self, name):
    self.name = name

from types import MethodType
x.setName = MethodType(setName, x)
x.setName('x')
print(x.name)

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
y = Student()
y.setName('y')

# 为了给所有实例都绑定方法，可以给class绑定方法
def setName(self, name):
    self.name = name

Student.
