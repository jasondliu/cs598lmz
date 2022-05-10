import mmap
+
+class mmap_wrapper:
+    '''
+    Provides a context-manager to use mmap-ed files as if they were normal
+    file-like objects.
+    '''
+
+    def __init__(self, filename, mode='r'):
+        self.filename = filename
+        self.mode = mode
+        self.file = open(filename, 'r+')
+        self.mmap = mmap.mmap(self.file.fileno(), 0, access=mmap.ACCESS_WRITE)
+
+    def __enter__(self):
+        return self.mmap
+
+    def __exit__(self, type, value, traceback):
+        self.mmap.close()
+        self.file.close()
+
+
+
+if __name__ == '__main__':
+    # Simple test
+    
+    with mmap_wrapper('test.mmap', 'w+') as m:
+        m.write(b"Hello world!")
+        m
