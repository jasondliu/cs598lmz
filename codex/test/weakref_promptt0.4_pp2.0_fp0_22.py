import weakref
# Test weakref.ref() with a callable object.
import weakref

class C(object):
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value

def f():
    return C(42)

r = weakref.ref(f())
print(r().value)
# Test weakref.ref() with a callable object, and test that
# the callable is called when the weakref is called.
import weakref

class C(object):
    def __init__(self, value):
        self.value = value

    def __call__(self):
        return self.value

def f():
    return C(42)

r = weakref.ref(f())
print(r().value)
# Test weakref.ref() with a callable object, and test that
# the callable is called when the weakref is called.
import weakref

class C(object):
    def __init__(self, value):
        self.value = value

