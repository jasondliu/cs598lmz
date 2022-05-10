import weakref
# Test weakref.ref on new-style class instances.
print("Test weakref.ref on new-style class instances.")

class C(object):
    pass

c = C()
c.foo = "bar"
print("c.foo=", c.foo)
ref = weakref.ref(c)

print("ref()=", ref())
print("ref().foo=", ref().foo)

del c
print("ref()=", ref())

print("Test weakref.weakvaluedict.")
# Test weakref.weakvaluedict
from weakref import weakvaluedict

wv = weakvaluedict()
wv["foobar"] = c
print("Contains foobar ?", "foobar" in wv)
print("Contains barfoo ?", "barfoo" in wv)

print("Test weakref.WeakKeyDictionary.")
from weakref import WeakKeyDictionary

class Foo(object):
    a = 10
    def __init__(self, b):
        self.b = b
