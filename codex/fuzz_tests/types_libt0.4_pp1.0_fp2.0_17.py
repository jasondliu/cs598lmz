import types
types.ClassType

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHi(self):
        print 'Hello, my name is', self.name

p = Person('Swaroop', 24)
p.sayHi()

# This short example can also be written as Person('Swaroop', 24).sayHi()

# Class and Instance Variables

class Robot:
    '''Represents a robot, with a name.'''
    # A class variable, counting the number of robots
    population = 0
    def __init__(self, name):
        '''Initializes the data.'''
        self.name = name
        print '(Initializing {})'.format(self.name)
        # When this person is created, the robot
        # adds to the population
        Robot.population += 1
    def die(self):
        '''I am dying.'''
        print '{} is being destroyed!'.format(self.name)
        Robot.population -= 1
        if Robot.population ==
