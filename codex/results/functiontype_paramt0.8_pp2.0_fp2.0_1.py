from types import FunctionType
list(FunctionType(b, globals(), 'blah')())

# c)
from types import FunctionType
def b1(x):
    def b2(y):
        return x(y)
    return b2
list(FunctionType(b1, globals(), 'blah1')(lambda x: x**2))

# d)
from types import FunctionType
def b1(x):
    def b2(y):
        return x(y)
    return b2
list(FunctionType(b1, globals(), 'blah2')(lambda x: x**3))

# e)
from types import FunctionType
def b1(x):
    def b2(y):
        return x(y)
    return b2
list(FunctionType(b1, globals(), 'blah3')(lambda x: x**4))

# f)
from types import FunctionType
def b1(x):
    def b2(y):
        return x(y)
    return b2
list(FunctionType(b1, globals(), 'blah4')(
