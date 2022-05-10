import weakref
# Test weakref.ref()

# Test weakref.ref() with a class
class Thing:
    pass

obj = Thing()
r = weakref.ref(obj)
assert r() is obj

# Test weakref.ref() with a function
def func():
    pass

r = weakref.ref(func)
assert r() is func

# Test weakref.ref() with a type
class SubThing(Thing):
    pass

r = weakref.ref(SubThing)
assert r() is SubThing

# Test weakref.ref() with an instance method
class C:
    def meth(self):
        pass

c = C()
r = weakref.ref(c.meth)
assert r() is c.meth

# Test weakref.ref() with a string
r = weakref.ref("foo")
assert r() == "foo"

# Test weakref.ref() with a number
r = weakref.ref(42)
assert r() == 42

# Test weakref.ref() with a tuple
r = weakref.ref
