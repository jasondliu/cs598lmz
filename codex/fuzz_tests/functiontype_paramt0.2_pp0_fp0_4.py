from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# FunctionType.__code__ is a read-only attribute
def f(): pass
try:
    f.__code__ = None
except TypeError:
    print('TypeError')

# FunctionType.__code__ is a read-only attribute
def f(): pass
try:
    del f.__code__
except TypeError:
    print('TypeError')

# FunctionType.__code__ is a read-only attribute
def f(): pass
try:
    f.__code__ = None
except TypeError:
    print('TypeError')

# FunctionType.__code__ is a read-only attribute
def f(): pass
try:
    del f.__code__
except TypeError:
    print('TypeError')

# FunctionType.__code__ is a read-only attribute
def f(): pass
try:
    f.__code__ = None
except TypeError:
    print('TypeError')

# FunctionType.__code__ is a read-only attribute
def f(): pass
try:
   
