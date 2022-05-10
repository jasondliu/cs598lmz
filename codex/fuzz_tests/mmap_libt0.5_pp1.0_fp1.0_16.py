import mmap
+
+
+class MMap(mmap.mmap):
+
+    def __init__(self, *args, **kwargs):
+        super(MMap, self).__init__(*args, **kwargs)
+        self.__name = args[0]
+
+    def __repr__(self):
+        return '<MMap: %s>' % self.__name
+
+    def __str__(self):
+        return self.__name
+
+
+def mmap_open(filename, *args, **kwargs):
+    return MMap(filename, *args, **kwargs)
+
+
+def mmap_close(mmap):
+    mmap.close()

