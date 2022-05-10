import weakref

class _Data:
    def __init__(self, data):
        self.data = data

class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class _LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = _Node(data)
        node.next = self.head
        self.head = node

class LRUCache:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = {}
        self.access = _LinkedList()

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def __getitem__(self, key):
        if key not in self:
            raise KeyError(key)
        self.access.add(key)
        return self.cache[key].data.data

    def
