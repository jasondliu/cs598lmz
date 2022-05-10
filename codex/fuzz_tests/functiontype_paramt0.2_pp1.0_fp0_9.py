from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f():
    pass
list(f.__code__)

# method objects
class C:
    def m(self):
        pass
list(C.m)

# builtin functions
list(len)

# builtin methods
list(str.replace)

# builtin types
list(int)

# builtin exceptions
list(Exception)

# frame objects
def f():
    list(f.__code__.co_varnames)
f()

# traceback objects
try:
    1/0
except Exception as e:
    tb = e.__traceback__
    list(tb)

# slice objects
list(slice(1, 2, 3))

# cell objects
def f():
    x = 1
    def g():
        return x
    return g.__closure__[0]
list(f())

# generator objects
def f():
    yield 1
list(f())

# module objects
list(sys)

