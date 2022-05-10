import weakref
# Test weakref.ref on a function
def foo(x):
    return x + 42
f = foo
ref = weakref.ref(f)
assert ref() is f
del f
assert ref() is None
# Test weakref.ref on a method
class Test(object):
    def foo(self, x):
        return x + 42
    def bar(self):
        return self.foo
t = Test()
ref = weakref.ref(t.bar())
assert ref() is t.foo
del t
assert ref() is None


class Test(object):
    def foo(self, x):
        return x + 42
    def __del__(self):
        pass
t = Test()
ref = weakref.ref(t.foo)
assert ref() is t.foo
del t
assert ref() is None


class Test(object):
    def foo(self, x):
        return x + 42
    def __del__(self):
        pass
t = Test()
ref = weakref.ref(t.foo)
assert ref() is t.foo
del t
assert ref
