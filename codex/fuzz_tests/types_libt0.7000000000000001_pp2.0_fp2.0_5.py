import types
types.MethodType

class Student(object):
    pass

s = Student()
# 动态给实例绑定一个属性
s.name = 'Michael'
print s.name

# 动态给实例绑定一个方法
def set_age(self, age):
    self.age = age
s.set_age = types.MethodType(set_age, s, Student)
s.set_age(25)
print s.age

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
print s.score

s2 = Student()
s2.set_score(99)
print s2.score

#
