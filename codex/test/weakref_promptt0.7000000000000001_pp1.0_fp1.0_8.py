import weakref
# Test weakref.ref() on old-style objects.
import weakref

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Foo(%s)' % self.name


class Bar:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Bar(%s)' % self.name

def callback(r):
    print('callback(%r)' % r)

f = Foo('f')
r = weakref.ref(f, callback)
print(r)
print(r())

f = Foo('f2')
print(r())

b = Bar('b')
print(r())

b = Bar('b2')
print(r())

# callback(<weakref at 0x1004e8ab8; to 'Foo' at 0x1004e8c88>)
# Foo(f)
# callback(<weakref at 0x1004e8ab8; dead>)
# None
