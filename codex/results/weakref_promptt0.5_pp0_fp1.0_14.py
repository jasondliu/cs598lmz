import weakref
# Test weakref.ref with a class that has a custom __del__ method.

class C:
    def __init__(self):
        self.a = 1

    def __del__(self):
        pass

    def __repr__(self):
        return 'C(%d)' % self.a

def f():
    c = C()
    r = weakref.ref(c)
    print(r())
    del c
    print(r())

f()
import weakref
# Test weakref.ref with a class that has a custom __del__ method.
# This test is a bit different from the previous one: the class
# has a __del__ method that deletes the instance.

class C:
    def __init__(self):
        self.a = 1

    def __del__(self):
        del self

def f():
    c = C()
    r = weakref.ref(c)
    print(r())
    del c
    print(r())

f()
import weakref
# Test weakref.ref with a class that has a
