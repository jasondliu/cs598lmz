import types
types.MethodType(foo, obj)

obj.foo = types.MethodType(foo, obj)
obj.foo()

# 类的实例也可以绑定方法，只是绑定的方法只能被实例调用
def bar(self):
    print('bar')

Student.bar = bar
s = Student()
s.bar()

# 绑定属性
s.name = 'Michael'
print(s.name)

# 绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 但是给一个实例绑定的方法，对另一个实例是不
