from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# __name__ is not a valid attribute for a function
def f(): pass
try:
    f.__name__ = 'foo'
except TypeError:
    pass
else:
    print('TypeError expected')

# __doc__ is not a valid attribute for a function
def f(): pass
try:
    f.__doc__ = 'foo'
except TypeError:
    pass
else:
    print('TypeError expected')

# __module__ is not a valid attribute for a function
def f(): pass
try:
    f.__module__ = 'foo'
except TypeError:
    pass
else:
    print('TypeError expected')

# __defaults__ is not a valid attribute for a function
def f(): pass
try:
    f.__defaults__ = 'foo'
except TypeError:
    pass
else:
    print('TypeError expected')

# __code__ is not a valid attribute for a function
def f(): pass
try:
    f.__code__ = 'foo'

