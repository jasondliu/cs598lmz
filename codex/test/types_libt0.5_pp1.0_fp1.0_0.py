import types
types.MethodType(func, obj)

# 给实例绑定属性
obj.age = 18
obj.age

# 给实例绑定方法
def set_age(self, age):
    self.age = age
obj.set_age = types.MethodType(set_age, obj)
obj.set_age(25)
obj.age

# 给类绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score
obj.set_score(100)
obj.score

# 给类绑定属性
Student.name = 'Student'
obj.name

# 限制实例的属性
class Student(object):
    __slots__ = ('name', 'age')
s = Student()
s.name = 'Michael'
s.age = 25
# s.score
