import weakref
# Test weakref.ref in isolation
class Tester(object):
    pass

def f(x):
    pass

def weakref_test():
    t = Tester()
    ref = weakref.ref(t, f)
    t.a = 1
    t.b = 2
    t.c = 3
