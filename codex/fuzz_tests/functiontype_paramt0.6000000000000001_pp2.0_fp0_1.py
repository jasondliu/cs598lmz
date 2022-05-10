from types import FunctionType
list(FunctionType(code, globals(), "foo"))

#
# Functions with annotations
#

def foo(a:int, b:str, c:(int, float)):
    return a, b, c

foo(1, "hello", (1, 2.0))

#
# Callable objects
#

class Foo:
    def __call__(self, a, b):
        return a, b

foo = Foo()
foo(1, 2)

#
# Functions with variable number of arguments
#

def bar(*args):
    return args

bar(1, 2, 3)

def bar2(a, *args, **kwargs):
    return a, args, kwargs

bar2(1, 2, 3, x=1, y=2)

#
# Functions with variable number of keyword arguments
#

def bar3(**kwargs):
    return kwargs

bar3(x=1, y=2)

#
# Functions with both variable number of arguments and keyword arguments
#

def bar4(*args,
