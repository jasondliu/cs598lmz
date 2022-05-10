import types
types.MethodType(myFunction, myObject)
myObject.myMethod()


# 动态增加属性
# class Student(object):
#     pass

# s = Student()

# s.name = 'Michael' # 动态给实例绑定一个属性
# print(s.name)

# def set_age(self, age):
#     self.age = age

# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的：
# s2 = Student()
# s2.set_age(25) # AttributeError: 'Student' object has no attribute 'set_age'

# 给类
