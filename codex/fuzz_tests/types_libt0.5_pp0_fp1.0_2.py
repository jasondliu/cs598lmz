import types
types.MethodType(f, None, Student)

class Student(object):
    pass

s = Student()
def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(100)
s.score

s2 = Student()
s2.set_score(99)
s2.score

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 99

class Student(object):
    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise Value
