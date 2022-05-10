import weakref
+
+
+class SparseArray(object):
+    def __init__(self, iterable, factory=int):
+        self.__map = weakref.WeakValueDictionary()
+        self.__factory = factory
+        self.extend(iterable)
+
+    def __getitem__(self, index):
+        if isinstance(index, slice):
+            return (self.__getitem__(i) for i in range(*index.indices(len(self))))
+        else:
+            try:
+                return self.__map[index]
+            except KeyError:
+                return self.__factory()
+
+    def __setitem__(self, index, value):
+        self.__map[index] = value
+
+    def __len__(self):
+        return max(self.__map.keys()) + 1
+
+    def __delitem__(self, index):
+        del self.__map[index]
+
+    def __repr__(self):

