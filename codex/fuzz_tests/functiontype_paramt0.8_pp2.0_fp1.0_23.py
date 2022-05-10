from types import FunctionType
list(FunctionType(abs))

# Should not be valid.
#list(FunctionType(1))
#list(FunctionType(list))

list(FunctionType(abs, globals()))
list(FunctionType(abs, globals(), 'myabs'))
list(FunctionType(abs, globals(), 'myabs', abs.__doc__))

list(FunctionType(abs, globals(), 'myabs', abs.__doc__, 0))

# Should not be valid.
#list(FunctionType(abs, globals(), 'myabs', abs.__doc__, 0, None))
#list(FunctionType(abs, globals(), 'myabs', abs.__doc__, 0, None, None))
#list(FunctionType(abs, globals(), 'myabs', abs.__doc__, 0, None, None, None))
#list(FunctionType(abs, globals(), 'myabs', abs.__doc__, 0, None, None, None, None))


# --------------------------------------------------------------------
# Test __init__ and __new__

# Bound method __init__.
list(type('
