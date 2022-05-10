import weakref
# Test weakref.ref() on a tuple.
class Foo(object):
    pass

class Bar(object):
    pass

def f(arg):
    print arg

a = Foo()
b = Bar()
t = (a, b)
r = weakref.ref(t, f)
print r()
del t
print r()
del a
print r()
del b
print r()
