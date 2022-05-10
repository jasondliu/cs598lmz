import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# if you want to get the name of a class or function, you can use __name__
print(type(func).__name__)
print(type(x for x in range(10)).__name__)

# Inspect Module
import inspect
print(inspect.getmembers(str))

def greet(name):
    return 'Hello, ' + name + '!'

print(inspect.getmembers(greet))

# you can even find out the source code of a function
print(inspect.getsource(greet))

# Python Object Relational Mapper
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.followers = []

    def add_follower(self
