import types
types.FunctionType

callable(add_three)
# Function are objects, hence they have type, varibale names etc.

add_three.__name__

# Function can return another function. Higher order functions
def make_adder(n):
    def adder(x):
        return x + n
    return adder

make_adder(4)(2)

# Function can capture the environment variables.
add_three.__code__.co_freevars

# Closure
def make_adder(n):
    def adder(x):
        return n + x
    return adder

# Three functions.
add_three.__code__.co_freevars
