from types import FunctionType
a = (x for x in [1])

b = (x for x in range(3))
b

# isinstance(a, FunctionType)
# isinstance(b, FunctionType)

# type(b)

# generator object
# generator object is an iterator

# isinstance(a, Iterator)
# isinstance(b, Iterator)

# yield makes a function a generator function

# in python3, range is an iterator itself
# in python2, range returns a list
# in python2, xrange is similar to range in python3

# generator is a function that uses yield
# generator function is a function that contains at least 1 yield statement

# generator expression:
# (x for x in range(3)), (x for x in range(3) if x % 2 == 0)

# Generator Expressions vs List Comprehensions
# Generator expressions don't create the entire list, but instead create a generator object.
# Generator expressions evaluate to an iterator that generates values as necessary, not
# all at once

# Iterators vs Iterables
# Iterators have 2 important methods: __next__ and __iter__
#
