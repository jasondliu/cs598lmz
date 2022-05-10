from types import FunctionType
list(FunctionType(lambda :1))

# Functions declared with def are not classes and can't be used as such.
#
# They can't be used in a isinstance() call either.

class A: pass

def f(): pass

isinstance(f, A)

isinstance(f, FunctionType)

# Input
#
# This function returns a value entered by the user.
# The value is always a string.

input('Enter a number: ')

# Return
#
# This keyword exits a function and returns a value.
# If the function has no return statement, it returns None.
# If the return statement has no argument, it will return None.

def add(a, b):
  return a + b

add(1,2)

# global
#
# This keyword is used to declare that a variable inside a function is global.
#
#
# It is used to modify the value of a global variable inside a function.
#
# It is used to access the value of a global variable inside a function.

def f():
  global x
  x = 1

