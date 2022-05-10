import types
types.ClassType

# 创建类
class Person:
    pass

# 创建对象
p = Person()

# 创建类
class Person:
    def sayHi(self):
        print('Hello, how are you?')

# 创建对象
p = Person()
p.sayHi()

# 创建类
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, my name is', self.name)

# 创建对象
p = Person('Swaroop')
p.sayHi()

# 创建类
class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
