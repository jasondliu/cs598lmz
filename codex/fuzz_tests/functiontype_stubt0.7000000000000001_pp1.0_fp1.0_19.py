from types import FunctionType
a = (x for x in [1])
type(a)

def foo():
    pass
type(foo)

type(abs)

class Animal():
    def __init__(self,name):
        self.name = name
    def run(self):
        print('Animal is running...')

a = Animal('dog')
a.run()

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(a)

class Cat(Animal):
    def run(self):
        print('Cat is running...')

c = Cat('cat')
c.run()
run_twice(c)

class Timer():
    def run(self):
        print('Start...')

t = Timer()
run_twice(t)

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

t = Tortoise('Totoro')
run_twice(t)

print(type(123))
print(type('str'))
print(type(None))
