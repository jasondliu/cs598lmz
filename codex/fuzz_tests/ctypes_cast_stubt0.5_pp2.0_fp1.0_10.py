import ctypes
ctypes.cast(id(int), ctypes.py_object).value

#%%
import sys
sys.getrefcount(1)

#%%
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
wref

#%%
a_set = {2, 3, 4}
wref()

#%%
wref() is None

#%%
import gc
gc.collect()

#%%
wref() is None

#%%
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

#%%
import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
sorted(stock.keys())

#%%
del catalog
sorted(stock.keys())


