from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type(x for x in range(10)))
print(type((x for x in range(10))))
print(type([]))
print(type([]).__name__)
print('-'*20)

class Animal(object):
    def run(self):
        print('Animal is running...')
a = Animal()
print(isinstance(a, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
print('-'*20)

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')
    def eat(self):
        print('Eating fish...')

dog = Dog()
cat = Cat()
dog.run()
dog.eat()
cat.run()

