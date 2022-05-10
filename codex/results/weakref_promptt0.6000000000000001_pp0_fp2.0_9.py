import weakref
# Test weakref.ref behaviour
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
aa = weakref.ref(a)           # create a weak reference
print(aa)                 # really a weakref object
print(aa())              # dereference

del a                   # remove the one reference
print(aa())              # entry was automatically removed

a = A(10)
aa = weakref.ref(a)
print(aa)
print(aa())

a = None
print(aa)
print(aa())

# Create a class with a method
class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for
