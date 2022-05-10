from types import FunctionType
list(FunctionType().__dict__.keys())

# ['__module__', '__doc__', '__init__', '__call__']
# We see two of these are methods we override in our function, __init__ and __call__.

# So, when you see these three dots, it is a call to the object's __call__ method, with whatever arguments are passed in.
# You can override this method in your classes too.
# This can be useful in many situations where you want a compact syntax for your own functions or methods.
