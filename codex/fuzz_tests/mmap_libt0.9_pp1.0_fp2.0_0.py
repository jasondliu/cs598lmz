import mmap
+from math import log
+from re import findall
+import matplotlib.pyplot as plt
+from numpy import arange
+
+class Subset(object):
+    def __init__(self, file, set_id):
+        self.file = file
+        self.set_id = set_id
+        # get set size
+        with open(file, 'r+') as f:
+            m = mmap.mmap(f.fileno(), 0)
+            string = m.readline()
+            self.cardinality = len(findall('\S+', string))
+        # find all permutations
+        self.permutations = list(permutations(range(self.cardinality), int(log(self.cardinality, 2))))
+
+    def __repr__(self):
+        return "Subset(%s)" % self.file
+
+    def __iter__(self):
+        with open(self.file, 'r+') as f:
+            m = mmap.
