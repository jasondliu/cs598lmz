import gc, weakref

class DictEntry(object):

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return '<DictEntry %s:%s>' % (self.key, self.value)

class Dict(object):

    def __init__(self):
        self.entries = [None] * 16
        self.size = 0

    def __setitem__(self, key, value):
        if self.size > len(self.entries) * 0.75:
            self.resize()
        n = self.hash(key) % len(self.entries)
        self.entries[n] = DictEntry(key, value, self.entries[n])
        self.size += 1

    def __getitem__(self, key):
        n = self.hash(key) % len(self.entries)
        e = self.entries[n]
        while e:

