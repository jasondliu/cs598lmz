import weakref
# Test weakref.ref()

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d())             # print the value via the reference
print(d() is a)        # reference objects compare like the objects they reference
print(d() == 10)       # and evaluate like the objects they reference
del a                  # remove the one reference
print(d() is None)     # the weak reference returns None

# Test weakref.WeakKeyDictionary

class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakKeyDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:

