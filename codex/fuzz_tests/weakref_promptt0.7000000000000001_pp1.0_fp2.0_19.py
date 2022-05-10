import weakref
# Test weakref.ref
class Foo:
    pass

# Create an instance of Foo and a weak reference to it.
f = Foo()
r = weakref.ref(f)
# Test weakref.proxy
class Foo:
    def __init__(self,x):
        self.x = x
    def m(self):
        return self.x

f = Foo(42)
# Create a weak reference to f.
p = weakref.proxy(f)
# Call f.m
print(f.m())
# Call p.m
print(p.m())
# Test weakref.finalize
def bar(x):
    print('Deallocating {}'.format(x))

class Foo:
    def __init__(self,x):
        self.x = x
        weakref.finalize(self, bar, self.x)
    def m(self):
        return self.x

f = Foo(42)
# Call f.m
print(f.m())
# Delete f
del f
# Test weakref.WeakSet
class Foo:
    pass

