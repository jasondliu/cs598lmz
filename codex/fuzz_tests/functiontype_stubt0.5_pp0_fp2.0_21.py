from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x:x+1))
print(type(FunctionType))

#实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

#使用__slots__
class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

#使用@property
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <
