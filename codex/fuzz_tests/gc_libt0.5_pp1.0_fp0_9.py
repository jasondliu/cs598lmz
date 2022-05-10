import gc, weakref

class WeakValueDictionary(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[key]()

    def __setitem__(self, key, value):
        self.store[key] = weakref.ref(value)

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

class MyClass(object):
    pass

def main():
    m = MyClass()
    d = WeakValueDictionary()
    d['a'] = m
    d['b'] = m
    print(list(d.items()))
    del m
    gc.collect()
    print(list(d.items()))


