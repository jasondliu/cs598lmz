import types
types.ClassType

# Question 6

def addTwo(x, y):
    return x + y

print addTwo(4, 7)

def doMath(a, b, fn = addTwo):
    return fn(a, b)

print doMath(4, 5)
print doMath(4, 5, lambda x, y: x * y)

# Question 7

class Person:
    def __init__(self):
        self.name = "Joe"
        self.age = 12

obj = Person()
obj.age = 21
print obj.age

# Question 8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

obj = Person("Joe", 12)
print obj.age
obj.birthday()
print obj.age

# Question 9

class Dog:
    def __init__(self, name):
        self.name = name

    def respondToName(self):
        return "
