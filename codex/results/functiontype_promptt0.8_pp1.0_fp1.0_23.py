import types
# Test types.FunctionType
if type(foo) is not types.FunctionType:
    raise ValueError, "foo should be of FunctionType"

# Test type of the return value of foo
if type(foo()) is not int:
    raise ValueError, "foo() should return an integer"

# Test __doc__
# We may want to add a test for ``foo.__doc__ == 'Does nothing. Returns 42.'``
# here.
foo.__doc__ = 'Does nothing. Returns 42.'
if foo() != 42:
    raise ValueError, "foo should return 42"

# Test calling foo with parameters; it should ignore them.
foo(1, 2, 3, 4, 5)
if foo() != 42:
    raise ValueError, "foo should return 42"

# Test __name__
if foo.__name__ != 'foo':
    raise ValueError, "foo should have a name"

foo.__name__ = 'bar'
if foo.__name__ != 'bar':
    raise ValueError, "foo should have a name"
if foo() != 42:
    raise ValueError
