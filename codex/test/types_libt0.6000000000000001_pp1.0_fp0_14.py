import types
types.FunctionType

x = types.FunctionType
type(x)

def my_function():
    return 'Hello world'

x = my_function
x
x()

class MyClass:
    def __init__(self):
        self.x = 10
    def my_method(self):
        return 'Hello world'

my_object = MyClass()
my_object.x
my_object.my_method()

x = MyClass.my_method
x
x(my_object)

x = my_object.my_method
x
x()

x = my_object.my_method()
x

def my_function():
    return 'Hello world'

x = my_function

def my_decorator(f):
    print(f)
    return f

my_function = my_decorator(my_function)
my_function()

@my_decorator
def my_function():
    return 'Hello world'

my_function()

