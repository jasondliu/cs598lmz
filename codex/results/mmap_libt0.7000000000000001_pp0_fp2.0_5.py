import mmap
+
+# Enable mmap for read-write file-like objects
+
+class mmap_rw(mmap.mmap):
+    def __new__(cls, *args, **kwargs):
+        obj = super(mmap_rw, cls).__new__(cls, *args, **kwargs)
+        if not obj._mmap.writeable():
+            obj._mmap.resize(obj.size())
+        return obj
+
+def mmap_rw_open(f, name):
+    return mmap_rw(f.fileno(), 0, access=mmap.ACCESS_WRITE)
+
+mmap.mmap = mmap_rw
+mmap.mmap.open = mmap_rw_open

