from types import FunctionType
list(FunctionType(lambda x : x * x, globals(), 'lambda'))

# __name__ is the name of the function
i.__name__

def print_name(func):
    def wrapper(*args, **kwargs):
        print("Function name is " + func.__name__)
        return func(*args, **kwargs)
    return wrapper

@print_name
def add(x, y):
    return x + y

add(2, 3)

# The @ syntax is equivalent to the following
add = print_name(add)

# Decorators can also be used as part of a class
class PrintName:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Function name is " + self.func.__name__)
        return self.func(*args, **kwargs)

@PrintName
def add(x, y):
    return x + y

add(1, 2)

# A decorator is a function that returns a function

