import weakref
# Test weakref.ref() and weakref.proxy() with various types of objects.
#
# Weak references to objects are created by calling the ref() function.
#
# Weak references to callable objects are created by calling the proxy()
# function.


class C:
    """A class with a __del__ method.
    """

    def __init__(self):
        self.foo = 'foo'

    def __del__(self):
        print('deleting C')


class D:
    """A class with a __del__ method that raises an exception.
    """

    def __del__(self):
        print('deleting D')
        raise RuntimeError


class E:
    """A class with a __del__ method that calls back into Python.
    """

    def __del__(self):
        print('deleting E')
        print(E.x)


def f():
    """A function with a __del__ method.
    """
    print('deleting f')


f.x = 'x'

del f


