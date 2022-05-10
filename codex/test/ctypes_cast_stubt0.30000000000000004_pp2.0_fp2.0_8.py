import ctypes
ctypes.cast(1, ctypes.py_object)

#import sys
#sys.getrefcount(1)

import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None)

import sys
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese

sorted(stock.keys())
del catalog
sorted(stock.keys())
del cheese
sorted(stock.keys())

print(sys.getrefcount(1))

import weakref
