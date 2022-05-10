import types
types.MethodType(lambda self: self.__class__.__name__, None)

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name

t = Teacher('Alice', 'Female', 'English')
s = Student('Bob', 'Male', 88)
print(isinstance(t, Person))
print(isinstance(t, Student))
print(isinstance(s, Person))
