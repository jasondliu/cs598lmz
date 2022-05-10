from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = [x for x in [1]]
print(type(a))
print(type(b))
print(type(c))
print(type(abs))
print(type(lambda x:x))
print(type((x for x in [1,2])))
print(type(isinstance))
print(type(FunctionType))

class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

class RunnableMixIn(object):
    def run(self):
        print('running.....')

class FlyableMixIn(object):
    def fly(self):
        print('flying...')

class Dog(Mammal,RunnableMixIn):
    pass

class Bird(Animal,FlyableMixIn):
    pass

class Myobject(object):
    def
