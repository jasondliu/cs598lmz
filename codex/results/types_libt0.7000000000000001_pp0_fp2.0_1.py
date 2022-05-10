import types
types.MethodType(lambda self: None, None, C)
 
'''

import types
from functools import partial


def foo():
    pass


def bar():
    pass


def foobar(func):
    def wrapper(self):
        print("Hello!")
        func(self)
        print("Bye!")

    return wrapper


class Foo:
    def __init__(self):
        self.foo = types.MethodType(foo, self)
        self.bar = types.MethodType(bar, self)
        self.foobar = types.MethodType(foobar(bar), self)


if __name__ == '__main__':
    f = Foo()
    f.foo()
    f.bar()
    f.foobar()

    # f2 = Foo()
    # f2.foobar()

    # f3 = Foo()
    # f3.foobar()
