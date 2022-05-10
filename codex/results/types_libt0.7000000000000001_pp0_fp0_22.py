import types
types.MethodType

class Student(object):
    pass

s = Student()
def set_age(self,age):
    self.age = age

s.set_age = types.MethodType(set_age,s)
s.set_age(25)
print s.age

#给一个实例对象绑定一个方法，对另一个实例对象不起作用
s2 = Student()
#s2.set_age(25)

#为了给所有实例绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print s.score
s2.set_score(99)
print s2.score

#通常情
