from types import FunctionType
list(FunctionType(max.__code__, globals(), 'max'))
 
# 'reversed' is a built-in function with its own implementation, written in C
# It cannot be accessed directly
# It is not an 'iterator' (rather an iterable)
# It is an 'iterator protocol'
# The protocol (interface) consists of __iter__ returning self, and next
# Reversed is a special-casing of the iterator protocol, that is efficient

# Generator functions are functions that when called, return a generator object
# that supports the iteration protocol
def fibonacci_generator():
    """
    Compute fibonacci numbers indefinitely.
    """
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, curr + prev

fib_gen = iter(fibonacci_generator())
next(fib_gen)
next(fib_gen)

# Example of list comprehension
def fibonacci_list(count):
    """
    Compute fibonacci numbers and return them as a list
    """

