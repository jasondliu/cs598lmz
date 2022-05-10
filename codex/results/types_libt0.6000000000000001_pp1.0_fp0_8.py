import types
types.MethodType

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eat ...')

    def sleep(self):
        print('sleep ...')

def play(self):
    print('play ...')

def drink(self):
    print('drink ...')

p = Person('Tom', 23)

p.eat()
p.sleep()

p.play = types.MethodType(play, p) # 动态添加方法
p.play()

Person.drink = drink # 给类添加方法
p.drink()
