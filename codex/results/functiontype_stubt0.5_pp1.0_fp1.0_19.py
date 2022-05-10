from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type(x for x in range(10)))
print(type(FunctionType))

print(type(type))

print(type(object))


class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')


dog = Dog()
dog.run()

cat = Cat()
cat.run()

tortoise = Tortoise()
tortoise.run()

print(isinstance(tortoise, Animal))
print(isinstance(tortoise, Tortoise))
print(isinstance(tortoise, Dog))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1,
