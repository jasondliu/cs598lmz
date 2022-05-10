import types
types.MethodType(f1,None,Dog)

class Dog(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print('%s is running...' % self.name)
        
d = Dog('dahuang')
d.game()
class Cat(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print('%s is running...' % self.name)
        
c = Cat('miaomiao')
c.game()

class Dog(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print('%s is running...' % self.name)
        
class Cat(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print('%s is running...' % self.name)
        
class Tortoise(object):
    def __init__(self, name):
        self.name
