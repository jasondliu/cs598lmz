import types
types.MethodType

def set_age(self,age):
    self.age=age
    
s.set_age=types.MethodType(set_age,s)

s.set_age(25)
print(s.age)

def set_score(self,score):
    self.score=score
    
Student.set_score=set_score

s.set_score(100)
print(s.score)

s2=Student('Bob',20)
s2.set_score(100)
print(s2.score)

class Student(object):
    __slots__=('name','age')#给实例绑定的属性
    
s=Student()
s.name='Alice'
s.age=20

try:
    s.score=99
except AttributeError as e:
    print('AttributeError:',e)

class GraduateStudent(Student):
    pass

g=GraduateStudent()
g.score=99
print(g.score)
