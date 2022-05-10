import types
# Test types.FunctionType
try:
    isinstance(my_abs, types.FunctionType)
    print('my_abs is a function.')
except NameError:
    print('my_abs is not a function.')

# Test types.UnboundMethodType
def hello_world():
    print('hello world')
hello_world_object = hello_world
if isinstance(hello_world_object, types.UnboundMethodType):
    print('hello_world_object is a unbound method.')
else:
    print('hello_world_object is not a unbound method.')



# isinstance() can also test user's defined class:
# Define a class named Animal:
class Animal(object):
    pass
# Define a class inherited from Animal:
class Dog(Animal):
    pass
# Create a dog object:
dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
# print(isinstance(dog, int)) # TypeError: int() takes at most 2 arguments (3 given)

# Exercise 1: write a function to judge
