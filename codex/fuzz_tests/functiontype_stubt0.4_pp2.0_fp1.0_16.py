from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def add(x,y):
    return x+y

print(add)
print(type(add))
print(type(add) is FunctionType)
print(type(abs) is FunctionType)
print(type(lambda x: x) is FunctionType)

print(dir(FunctionType))
print(dir(abs))

print(callable(add))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))

print(hasattr(abs, '__call__'))

class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()
print(callable(s))

print('----------------')

def fn(self, name='world'):
    print('Hello, %s.' % name)

Hello
