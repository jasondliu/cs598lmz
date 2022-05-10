import types
types.MethodType

class Student(object):
    pass

s = Student()
def set_age(self,age):
    self.age = age

s.set_age = types.MethodType(set_age,s)
s.set_age(25)
