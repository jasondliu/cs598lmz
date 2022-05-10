import ctypes
ctypes.cast(id(my_func), ctypes.py_object).value

# ctypes.cast(id(my_func), ctypes.py_object).value
print(id(my_func) == id(my_func))
my_func is my_func
 
# Comparing functions
print(id(my_func) == id(inc))
print(my_func is inc)
 
# Comparing different objects
print(id(my_func) == id(lambda x: x + 1))
print(my_func is (lambda x: x + 1))
 
# my_func and inc are two names for the same function object
print( my_func.__name__ == inc.__name__ )
print( my_func.__doc__ == inc.__doc__ )
 
# Functions are first class
def executor(func):
    return func(2)
 
 
executor(inc)
executor(my_func)
executor(lambda x: x + 1)
 
# Incorrect number of arguments
try:
    executor()
except TypeError
