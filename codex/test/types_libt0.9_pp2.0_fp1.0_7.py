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
