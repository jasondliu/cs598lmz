import mmap
+import os
+import sys
+
+
+def main():
+
+    if len(sys.argv) != 2:
+        print "usage: %s <file>\n" % sys.argv[0]
+        sys.exit(2)
+
+    fname = sys.argv[1]
+
+    if not os.path.isfile(fname):
+        print "file does not exist %s" % fname
+        sys.exit(1)
+
+    f = open(fname, "r+")
+
+    # memory map the file, size 0 means whole file
+    mm = mmap.mmap(f.fileno(), 0)
+
+    print "File before: ", mm[:]
+
+    # read content via standard file methods
+    print "First      :", mm.readline()
+
+    # read content via slice notation
+    print "Second     :", mm[4:10]
+
+    # update content using slice notation;
+    # note that
