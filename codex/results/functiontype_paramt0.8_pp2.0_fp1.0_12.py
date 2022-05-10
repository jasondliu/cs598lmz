from types import FunctionType
list(FunctionType(Func.__code__, globals(), 'FunctionType_name'))

"""
Class function
"""

class A:
    def __init__(self):
        print("Init class")
        
def class_func(cls):
    print("Entered")
    return cls()

a = class_func(A)

""" Decorators """
def decorator_f(func):
    def wrap_func():
        print("Before")
        func()
        print("After")
    return wrap_func

def print_f():
    print("Hello")

print_f = decorator_f(print_f)
print_f()

@decorator_f
def print_f():
    print("Hello")
    
print_f()

""" Decorator with argument """

def decorator_f(func):
    def wrap_func(*args,**kwargs):
        print("Before")
        func(*args,**kwargs)
        print("After")
    return wrap_func

@decorator_f
def
