from types import FunctionType
list(FunctionType(lambda: None).__code__.co_freevars)

# But these don't
list(FunctionType(lambda: None).__code__.co_varnames)
list(FunctionType(lambda: None).__code__.co_cellvars)

# In Python 3.0, the result of compile() has the same attributes as the code object
# returned from exec or from the built-in function compile(). This change makes it
# possible to transparently use the output of compile() as the second argument to
# the built-in function exec().
code.co_varnames
code.co_cellvars
code.co_freevars

"""Recursion"""
# Recursive Functions

def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(42)

fact = factorial
fact
fact(5)
map(factorial, range(11))
list(map(factorial, range(11
