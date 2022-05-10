import ctypes
ctypes.cast(id(0), ctypes.py_object).value

# Create a function that takes an argument x and returns 2 * x + 1

def f(x):
    return 2*x + 1

# Create a function that takes an argument x and returns x2 + 3x + 1

def g(x):
    return x**2 + 3*x +1

# Create a function that takes in a string called name and prints out "Hello ____, how are you doing today?".

def hello(name):
    print('Hello ' + name + ', how are you doing today?')

# Using the same function, make it print "Hello Mr. " + name if the last letter of name is "n".

def hello(name):
    if name[-1] == 'n':
        print("Hello Mr. " + name + ', how are you doing today?')
    else:
        print('Hello ' + name + ', how are you doing today?')

# Create a function called exponent that takes in two arguments m and k and returns m ** k.

