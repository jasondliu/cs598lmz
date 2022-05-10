import types
types.MethodType(f, None, Greeter)  # Returns a function
# The function f is bound to the class Greeter
# When we call the function f, it's as if we called Greeter.f
f()  # The bound method f is called
# This is the output -
# Hello, World!

g = Greeter()
f(g)  # The bound method f is called
# This is the output -
# Hello, World!

f.__self__
# This is the output -
# <__main__.Greeter object at 0x7fe5c6e5b6d8>

f.__func__
# This is the output -
# <function Greeter.f at 0x7fe5c6e5b400>

f.__self__ is g
# This is the output -
# True

f.__func__ is Greeter.f
# This is the output -
# True

class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
       
