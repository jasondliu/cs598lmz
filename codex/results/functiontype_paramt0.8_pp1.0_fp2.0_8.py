from types import FunctionType
list(FunctionType(my_function, globals()).__code__.co_varnames)

# Another way to get the names of a function's arguments
# is to use inspect.getfullargspec
import inspect
inspect.getfullargspec(my_function)

# Instead of using a builtin, we can also define functions
# using the function keyword.
def add_function(x, y):
    return x + y

add_function(1, 2)

# With this syntax we can assign a function to a variable
add = add_function
add(3, 4)

# Or even pass it as an argument
def call_function(func, x, y):
    return func(x, y)

call_function(add, 5, 6)

# This means we can even define functions that return other functions
def make_adder(x):
    def add(y):
        return x + y
    return add

add_five = make_adder(5)
add_five(7)

# This can be confusing at first. If you have a hard time understanding
# this
