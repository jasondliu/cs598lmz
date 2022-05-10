from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)

# ([PEP8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
#  recommends using `snake_case` for variables and functions,
#  but we will follow the convention of using `PascalCase` for classes
#  and `camelCase` for functions and variables.)
def fooBar(a):
    return a + a

list(fooBar.__code__.co_varnames)

def fooBar(a, b):
    return a * b

list(fooBar.__code__.co_varnames)

# It is not possible to get the variable names for a function in the body
# of a function.  This is because the variables are not stored in the
# function's `__code__` object.
def fooBar(a, b):
    def qux(x):
        return a * x - b * x
    return qux

list(fooBar.__code__.co_v
