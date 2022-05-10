import gc, weakref

class Node(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

