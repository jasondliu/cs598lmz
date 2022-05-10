import types
types.MethodType

print(Student2.say_hi)
print(Student2.say_hi)
def f(self):
    print('f call')

print(Student2.__dict__)
Student2.run = f
Student2.run('Python')
Student2.run(23)
Student2.__dict__['run']
Student2.run
print(dir(object))
Student2.in_name
Student2.__dict__
Student2.__in_name = 'wwww'
Student2.__dict__
Student2.in_name
del Student2.__in_name
Student2.__dict__
'__name__' in Student2.__dict__
'__name__' in dir(Student2)

#__getattr__
class Student3(object):
    name = 'Student'
    def __init__(self, name):
        self.name = name
        print('init')
    def __getattr__(self, attr):
        if attr=='score':
            return 99

print(Student3('name').name
