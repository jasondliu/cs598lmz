from types import FunctionType
list(FunctionType(x) for x in range(2))

# Ensure that we are making the right type of exception for recursive
# generators.  This used to be a TypeError, now it's a RuntimeError.
def f():
    yield f()
list(f())

# Ensure that we're setting __name__ correctly.
def foo(): yield 1
g = foo()
g.__name__

# Test that the generator iterator is not its own class.
def foo(): yield 1
g = foo()
g.__class__ is type(g)

# Test that dir(generator) contains '__name__'.
def foo(): yield 1
g = foo()
'__name__' in dir(g)

# Test getattr(generator)
def foo(): yield 1
g = foo()
getattr(g, '__class__')

# Test that dir(generator) contains '__class__'
def foo(): yield 1
g = foo()
getattr(g, '__class__')

# Test that dir(generator) contains 'gi_code'
def foo(): yield 1

