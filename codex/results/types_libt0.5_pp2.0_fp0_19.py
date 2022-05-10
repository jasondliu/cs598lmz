import types
types.ModuleType.__doc__ = '''
A module is a file containing Python definitions and statements.
The file name is the module name with the suffix .py appended.
Within a module, the module's name (as a string) is available as the value of the global variable __name__.
For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents:

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

Now enter the Python interpreter and import this module with the following command:

>>> import fibo

This does not enter the names of the functions defined in fibo directly in the current symbol table; it only
