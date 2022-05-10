import types
types.MethodType(fn, Student())
# 实例对象可以调用实例方法，也可以调用类的方法
Student.sayHello()
Student().sayHello()
Student().sayHello = types.MethodType(fn, Student())
Student().sayHello()

# __slots__魔法
# def fn(self):
#     print('fn')
# Student.sayHello = fn
# Student().sayHello()
# 动态给实例添加方法，会报错

class Person(object):
    __slots__ = ('name', 'age', 'sayHello')
    pass
p = Person()
p.name = 'yuanhao'
p.age = 18

class Animal(object):
    __slots__ = ('name', 'age')
    pass
class Cat(Animal):
    pass
class Dog(Animal):
    __slots
