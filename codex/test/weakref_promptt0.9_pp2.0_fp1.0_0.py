import weakref
# Test weakref.reference calls in boolean context.
pass
class Foo(object):
    pass


#
class CallableFoo(object):
    pass


def weak_callable_test():
    c = weakref.WeakMethod(CallableFoo())
    return c()
#
import weakref as _weakref


class X(object):

    def __init__(self):
        self.l = []

    def __del__(self):
        self.l.append(1)


# test weak reference methods
class R:

    def __eq__(self, other):
        return True


#
# Test status of weakrefs
class C:

    def __init__(self, n):
        self.x = n

    def __eq__(self, other):
        return self.x == other.x


#
# test weak callable proxy methods
class Cc:

    def __init__(self, data):
        self.data = data

    def __call__(self, *args):
        return self.data


def f(x):
    return
