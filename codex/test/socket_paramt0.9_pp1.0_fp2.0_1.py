import socket
socket.if_indextoname(number)

#sets are unordered with no duplicate elements
#frozen set is just an immutable version of a Python set object
#dict comprehensions
{x:x**2 for x in range(5)}

#generator expressions: [] - list comprehensions, {} - dictionary comprehensions, () - generator expressions
#a generator is like a list comprehension, except it generates values just in time, instead of all at once into a list.

#decorators - a function that takes another function and extends the behaviour of the latter function without explicitly modifying it.
#@ symbol is used to apply decorator to a function
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapped before executing {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

