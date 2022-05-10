import gc, weakref
+
+
+class Node:
+    __slots__ = 'val', 'prev', 'next', 'key'
+
+    def __init__(self, key, val, prev=None, next=None):
+        self.key = key
+        self.val = val
+        self.prev = prev
+        self.next = next
+
+
+class LRUCache:
+
+    def __init__(self, capacity):
+        self.capacity = capacity
+        self.head = Node(0, 0)
+        self.tail = Node(0, 0)
+        self.head.next = self.tail
+        self.tail.prev = self.head
+        self.cache = {}
+
+    def get(self, key):
+        node = self.cache.get(key)
+        if not node:
+            return -1
+        self._remove(node)
+        self._add(node)
+        return node.val
+
+    def put(self, key, value):
+
