import types
# Test types.FunctionType to check whether it is true for functions
# Note: In Python 3, the names unicode and long does not exist,
#       instead we have just str and int

def f(x, y):
    print("hello")

#type(f)

def g(x, y):
    return "{0} value is: {1}".format(x, y)

x = g("x", 1)
print("g(x, 1) is: ", x)

#Defining generator functions

def gen_function_1():
    yield 1
    yield 2
    yield 3

def gen_function_2():
    yield 2
    yield 3
    yield 4
