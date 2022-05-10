import types
types.MethodType

class Student(object):
	pass

s = Student()

def set_age(self, age):
	self.age = age

s.set_age = types.MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
	self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)

s2 = Student()
s2.set_score(99)
print(s2.score)

class Student(object):
	__slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

class GraduateStudent(Student):
	pass

g = GraduateStudent()
g.score = 99
print(g.score)

class Student(object):
	def get_score(self):
		return self._score

	def set_score(self, value):
	
