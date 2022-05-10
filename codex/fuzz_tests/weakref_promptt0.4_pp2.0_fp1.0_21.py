import weakref
# Test weakref.ref
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)              # create a reference
d = weakref.ref(a)     # create a weak reference to it
print(d)               # get the object if it is alive
print(d())
del a                 # remove the one reference
print(d)               # it's gone, d is dead
print(d())

# Test weakref.WeakValueDictionary
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
sorted(stock.keys())
del catalog
sorted(stock.keys())
