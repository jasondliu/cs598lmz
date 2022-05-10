from types import FunctionType
list(FunctionType(lambda x: x, globals(), "lambda"))

# code objects
def f(): pass
def g(): pass
def h(): pass

list(f.__code__)
list(g.__code__)
list(h.__code__)

# frame objects
def f():
    def g():
        1/0
    try:
        g()
    except ZeroDivisionError:
        import sys
        return sys.exc_info()[2].tb_frame

tb = f()
list(tb)

# traceback objects
def f():
    def g():
        1/0
    try:
        g()
    except ZeroDivisionError:
        import sys
        return sys.exc_info()[2]

tb = f()
list(tb)

# slice objects
list(slice(1, 10, 2))

# cell objects
def f():
    x = 42
    def g():
        return x
    return g.__closure__[0]

list(f())

# module objects
import
