import weakref
# Test weakref.ref on callable objects that are described by a function
# object.

class Callable:
    def __call__(self):
        pass


def method(self):
    pass


def g():
    pass


c = Callable()
r = weakref.ref(c)
r().__call__()
bound = c.__call__
r = weakref.ref(bound)
r()
r = weakref.ref(method)
r()
r = weakref.ref(g)
r()
