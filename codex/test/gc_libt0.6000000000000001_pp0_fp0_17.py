import gc, weakref
from collections import OrderedDict

class LinkedListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        self.head = LinkedListNode(0, 0)
        self.tail = LinkedListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

