import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
import sys
sys.getrefcount(x)

#%%
y = x
sys.getrefcount(x)

#%%
del x
sys.getrefcount(y)

#%%
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
wref

#%%
wref()

#%%
a_set = {2, 3, 4}
wref()

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
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'),
           Cheese('Brie'), Cheese('Parmesan')]
for cheese in catalog:
    stock[cheese.kind] = cheese
sorted(stock
