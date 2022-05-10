import types
types.ClassType

class MyClass:
    pass

type(MyClass)

class MyClass:
    def __init__(self, value):
        self.value = value

my_instance = MyClass('hello')
my_instance.value

class MyClass:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'MyClass(%s)' % self.value

my_instance = MyClass('hello')
str(my_instance)
print(my_instance)

class MyClass:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'MyClass(%s)' % self.value
    def __repr__(self):
        return str(self)

my_instance = MyClass('hello')
print(my_instance)

class MyClass:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'MyClass(%s
