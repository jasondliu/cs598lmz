import gc, weakref, gc, os, shutil
+
+# Ensure that we don't "lose" the id of a temporary file
+
+class MyFile:
+    def __init__(self, fname, mode):
+        self.f = open(fname, mode)
+    def close(self):
+        self.f.close()
+    def __del__(self):
+        print "Deleted", self
+
+f = MyFile("tempfile.txt", "w")
+del f
+print os.path.exists("tempfile.txt")
+
+# Keep track of all objects in a list
+
+class ObjectTracker:
+    def __init__(self):
+        self.lst = []
+    def add(self, obj):
+        self.lst.append(obj)
+    def remove(self, obj):
+        self.lst.remove(obj)
+    def __del__(self):
+        print "Deleting", self
+        for o in self.lst:
+           
