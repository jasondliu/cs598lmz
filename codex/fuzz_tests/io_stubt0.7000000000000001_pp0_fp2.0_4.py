import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

view = None


"""
    >>> def f():
    ...     x = 1
    ...     def g():
    ...         return x
    ...     return g
    ...
    >>> foo = f()
    >>> foo.__code__.co_freevars
    ('x',)
"""

def f():
    x = 1
    def g():
        return x
    return g

foo = f()
foo.__code__.co_freevars
del foo

def f(x):
    def g(y):
        return x + y
    return g

f(1)(2)

def f(x):
    def g(y):
        return x + y
    return g

f(1).__code__.co_freevars

def f(x):
    def g(y):
        return x + y
    return g

f(1).__closure__[0].cell_contents

def f(x):
    def g(y):
        return x + y
    return g

foo =
