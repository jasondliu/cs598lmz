import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

#5.3.3
import sys
sys.getrefcount(obj)

#5.3.4
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
wref
wref()
a_set = {2, 3, 4}
wref()

#5.3.5
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
sorted(stock.keys())
del catalog
sorted(stock.keys())
del cheese
sorted(stock.keys())

#5.3.6
import weakref
s1 = {
