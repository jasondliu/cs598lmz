import weakref
# Test weakref.ref() for class methods

class Foo:
    def __init__(self, i):
        self.i = i
    def bar(self):
        return self.i
    def baz(self, j):
        return self.i + j

foo = Foo(42)

r1 = weakref.ref(foo.bar)
r2 = weakref.ref(foo.baz)

print(r1(), r2(1))
foo = None
try:
    print(r1(), r2(1))
except ReferenceError:
    print('ReferenceError')
