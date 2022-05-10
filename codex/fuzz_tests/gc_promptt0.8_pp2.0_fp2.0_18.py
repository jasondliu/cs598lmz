import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() to run the garbage collection.
# Weakrefs with callbacks
def callback(n):
    print('preparing to clean up {}'.format(n))
class A:
    def __init__(self):
        self.n = 42
        self.wr = weakref.ref(self, callback)
a = A()
print('created {}'.format(a))
print('deleting {}'.format(a))
del a
gc.collect(); print('collected')

# weakref.WeakValueDictionary
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brick'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
    print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
