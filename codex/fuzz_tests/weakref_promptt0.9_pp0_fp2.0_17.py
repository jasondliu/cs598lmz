import weakref
# Test weakref.ref() can be chained.
class C(object):
    def __del__(self):
        pass

class D(object, C):
    pass

foo = D()
r = weakref.ref(foo)
wr = weakref.ref(r)
print wr()()
# Test weakref.ref() can be chained.
import weakref
# Test weakref.ref() can be chained.

def outer(obj):
    def inner():
        return lambda: obj

    return inner()

r = outer(1)
print r()
# Test weakref.ref() can be chained.
import weakref
# Test weakref.ref() can be chained.

bar = 1
def foo():
    return bar
wr = weakref.ref(foo)
print wr()()
print wr()()
# Test weakref.ref() can be chained.
import weakref
# Test weakref.ref() can be chained.

class A(object):
    x = "foo"

def f(x, y):
    return x
wr = weakref.ref(f)
