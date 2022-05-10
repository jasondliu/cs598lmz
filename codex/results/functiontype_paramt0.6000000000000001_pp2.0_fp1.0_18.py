from types import FunctionType
list(FunctionType(f.func_code, globals(), 'f1'))

#Classes
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, my name is', self.name
p = Person('Swaroop')
p.sayHi()
Person('Swaroop').sayHi()

#Classes and functions
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, my name is', self.name
p = Person('Swaroop')
p.sayHi()
Person('Swaroop').sayHi()

#Documentation
class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializing %s)' % self.name

        # When this person is created, he/she
        # adds to the population
        Person.population += 1
