import types
types.MethodType(lambda self: None, None, None)

# classes
class C:
    pass

class D(C):
    pass

# functions
def f(): pass

def g(x): return x

def h(x, y=42): return (x, y)

# generators
def gen():
    yield 1

# nested scopes
def scope():
    x = 12
    def nested():
        return x

# closures
def closure1():
    x = 12
    def nested():
        return x
    return nested

# builtins
len([1, 2, 3])

# exceptions
try:
    1/0
except ZeroDivisionError:
    import sys
    sys.exc_info()
finally:
    pass

# try/except/finally
try:
    1/0
except ZeroDivisionError:
    import sys
    sys.exc_info()
finally:
    pass

# with
with open(__file__) as f:
    f.read()

# imports
import sys

