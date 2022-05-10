from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x

list(f.__code__)

# method objects
class C:
    def m(self, x):
        return x

list(C.m)

# generator objects
def g():
    yield 1
    yield 2

list(g())

# traceback objects
try:
    raise Exception()
except Exception as e:
    list(e.__traceback__)

# frame objects
def f():
    list(f.__code__.co_freevars)

f()

# slice objects
list(slice(1, 2, 3))

# module objects
list(sys)

# class objects
list(C)

# method-wrapper objects
list(C.m)

# builtin-function objects
list(len)

# builtin-method objects
list(list.append)

# method-descriptor objects
list(list.__dict__['append'])

# getset-
