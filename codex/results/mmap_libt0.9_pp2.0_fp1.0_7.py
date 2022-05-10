import mmap
+import argparse
+
+class Variabile:
+    def __init__(self, nome, size, alloc, value, offset, initialized, addr, type, mtype=''):
+        self.nome = nome
+        self.size = size
+        self.alloc = alloc
+        self.value = value
+        self.offset = offset
+        self.initialized = initialized
+        self.addr = addr
+        self.type = type
+        self.mtype = mtype
+        pass
+
+def offset_from_addr(addr):
+    # TODO: check file type
+    # We suppose we are using ELF
+    cwd = os.getcwd()
+    for f in os.listdir(cwd):
+        fname, ext = os.path.splitext(f)
+        if ext == '.so':
+            #print "Processing: " + f
+            #print addr
+            fd = open(f, "r")
+            s = mmap.mmap(
