from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
def f(x):
    return x

list(f.__code__)

# method objects
class C:
    def m(self):
        pass

list(C.m)

# generator objects
def g():
    yield 1

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

list(f.__code__.co_freevars)

# memoryview objects
list(memoryview(b'abc'))

# dict proxy objects
list(type.__dict__)

# set objects
list(set([1, 2, 3]))

# frozenset objects
list(frozenset([1, 2, 3]))

# array objects
list(array('i', [1, 2, 3]))

# deque objects
list(deque([
