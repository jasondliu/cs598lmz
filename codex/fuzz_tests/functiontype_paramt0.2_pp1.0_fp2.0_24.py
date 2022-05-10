from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x
list(f.__code__)

# method objects
class C:
    def f(self, x):
        return x
list(C.f)

# generator objects
def g():
    yield 1
    yield 2
list(g())

# traceback objects
try:
    1/0
except:
    tb = sys.exc_info()[2]
    list(tb)

# frame objects
def f(x):
    return x
f.__code__.co_firstlineno
f.__code__.co_varnames
f.__code__.co_argcount

# slice objects
list(slice(1, 10, 2))

# xrange objects
list(xrange(1, 10, 2))

# NotImplementedType
list(NotImplemented)

# Ellipsis
list(Ellipsis)

# builtin_function_or_method
list(len)

