import types
types.MethodType(get_age,c)

#绑定方法
c.get_age = types.MethodType(get_age,c)
c.get_age()

#给类绑定方法
Student.get_age = get_age
s = Student()
s.get_age()

#限制类的属性
class Person(object):
    __slots__ = ('name','age')
    pass

p = Person()
p.name = 'Michael'
p.age = 25
#p.score = 99

class GraduateStudent(Person):
    pass

g = GraduateStudent()
g.score = 99

#使用@property
class Student(object):
    @property
    def score(self):
        return self._score
