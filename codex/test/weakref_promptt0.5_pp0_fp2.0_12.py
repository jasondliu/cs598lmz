import weakref
# Test weakref.ref()

class Foo:
    pass

f = Foo()
r = weakref.ref(f)
print(r)
print(r())

f = None
print(r())

r = None
print(r)

# Test weakref.finalize()

def bye():
    print('Gone with the wind...')

obj = Foo()
f = weakref.finalize(obj, bye)
print(f.alive)

del obj
print(f.alive)

f()
print(f.alive)

f = None
print(f)

# Test weakref.WeakKeyDictionary()

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakKeyDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese]
