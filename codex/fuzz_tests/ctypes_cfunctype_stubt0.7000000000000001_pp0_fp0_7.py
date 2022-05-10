import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
fun()

# What type does a function have?
def fun():
    pass
print(type(fun))

# Define a function that takes an
# object as input
def do_nothing(obj):
    pass

# What is the type of do_nothing?
print(type(do_nothing))

# Functions can be used as input arguments
# for a function
def call_fun(f):
    f()

# Call it
call_fun(fun)

# Function as input arguments
def call_fun(f):
    f()

# Define a function and call
def fun():
    print("inside fun")
call_fun(fun)

# Functions are first class citizens in Python
# and can be used like any other object
# Define a function
def f():
    print('inside f')

# Assign it to a variable
g = f

# Call it via the variable
g()

# Define a function
def h(x):
    print('inside h: ' + str(x))

# Call it
h
