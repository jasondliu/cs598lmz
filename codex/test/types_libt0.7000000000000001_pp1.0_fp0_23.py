import types
types.ClassType
# >>> types.TypeType
# >>> types.ObjectType

class Student(object):
    def say(self):
        print('hello')

s = Student()
s.say()

# s.print()

# isinstance(s, Student)

class A(object):
    def __init__(self):
        self.name = '1'
        self.age = 10

class B(A):
    def __init__(self):
        A.__init__(self)
        self.name = '2'
        self.grade = '100'

b = B()
print(b.name, b.age, b.grade)
