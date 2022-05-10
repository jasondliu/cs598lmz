import types
types.MethodType(test,None)

class Animal:
    pass

class Bird(Animal):
    pass

class Mammal(Animal):
    pass

class Runable:
    def run(self):
        print 'Run'

class Flyable:
    def fly(self):
        print 'Fly'

class Dog(Mammal,Runable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Runable):
    pass
