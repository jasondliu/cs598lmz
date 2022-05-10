import weakref
# Test weakref.ref() with a bound method.

class Foo(object):
    def __init__(self, value):
        self.value = value
    def meth(self, arg):
        return arg

def bar(arg):
    return arg

# Create instances
foo1 = Foo(1)
foo2 = Foo(2)
foo3 = Foo(3)

# Create some references to bound methods
foo1_meth = foo1.meth
foo2_meth = foo2.meth
foo3_meth = foo3.meth

# Create some weak references
wfoo1_meth = weakref.ref(foo1.meth)
wfoo2_meth = weakref.ref(foo2.meth)
wfoo3_meth = weakref.ref(foo3.meth)

# Try calling the methods
print foo1_meth('foo1_meth')
print foo2_meth('foo2_meth')
print foo3_meth('foo3_meth')

print wfoo1_meth('wfoo1
