from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x

list(f.__code__)

# frame objects
import sys

def f(x):
    return sys._getframe()

list(f(1))

# traceback objects
import sys

def f(x):
    raise Exception

try:
    f(1)
except Exception:
    list(sys.exc_info()[2])

# slice objects
list(slice(1, 2, 3))

# cell objects
def f(x):
    def g(y):
        return x + y
    return g

list(f(1).__closure__[0])

# generator objects
def f(x):
    yield x

list(f(1))

# module objects
list(sys)

# class objects
class C:
    pass

list(C)

# method objects
class C:
    def f(self):
        pass

list(C.f)

# un
