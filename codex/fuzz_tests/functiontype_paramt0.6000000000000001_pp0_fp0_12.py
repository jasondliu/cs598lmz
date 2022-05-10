from types import FunctionType
list(FunctionType(sum, globals(), "sum"))

# But we can get a list of the argument names, using the function's __code__ attribute:
sum.__code__.co_varnames

# Finally, we can get a list of the local variables in a function, using its __code__.co_varnames attribute:
sum.__code__.co_varnames

# We can also get the global variables and builtins used by a function:
sum.__code__.co_nlocals
sum.__code__.co_names

# And we can get the source code for a function, if available:
import dis
dis.dis(sum)

# We can even modify a function's behavior, by changing one of its attributes:
def hello(name):
    return "Hello " + name
hello.__name__
hello.__name__ = "hi"
hello("Guido")

# We can also attach arbitrary attributes to user-defined functions:
hello.author = "Brian K. Jones"
hello.author

# And we can attach functions to classes:
def goodbye(name):
