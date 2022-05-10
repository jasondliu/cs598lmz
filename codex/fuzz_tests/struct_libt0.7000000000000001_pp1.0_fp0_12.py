import _struct
+
+class MemoryView(object):
+    def __init__(self, base, size):
+        self.__base = base
+        self.__size = size
+    def __len__(self):
+        return self.__size
+    def __getitem__(self, index):
+        if isinstance(index, slice):
+            start, stop, step = index.indices(self.__size)
+            return self.__class__(self.__base + start, stop - start)
+        if not 0 <= index < self.__size:
+            raise IndexError('Index out of range')
+        return _struct.unpack_from('B', self.__base, index)[0]
+
+def sizeof(obj, seen=None):
+    seen = seen or set()
+    size = sys.getsizeof(obj)
+    if id(obj) in seen:
+        return 0
+    seen.add(id(obj))
+    if isinstance(obj, (tuple, list, set, frozenset
