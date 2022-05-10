import types
types.new_class("Person")

# --------------------------------------

# Class with inheritance
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("BARK BARK")

class Mutt(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

# --------------------------------------

# Class with multiple inheritance
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("zZzZzZZzzz")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

