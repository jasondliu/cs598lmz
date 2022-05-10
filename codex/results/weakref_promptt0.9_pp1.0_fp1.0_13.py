import weakref
# Test weakref.ref(kvstore) == kvstore.storage
# Test weakref.ref(d) == d.
import gc

class KeyValueStored:
    # This class holds an integer and weakly references a dictionary
    def __init__(self):
        self.d = {}
        self.storage = weakref.ref(self.d)
        self.i = 0

    def __del__(self):
        self.d[self.i] = self.i

for i in range(10):
    x = KeyValueStored()
    if wea
