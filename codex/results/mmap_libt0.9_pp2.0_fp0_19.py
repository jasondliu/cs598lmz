import mmap
+import math
+import argparse
+import datetime
+
+
+def add_cls(filename):
+    """
+    TODO: update docstring
+    Args:
+        filename (str): A string
+
+    Returns:
+        (bool): A boolean
+
+    """
+    with open(filename, "r+") as fp:
+        # Memory-map the file
+        mm = mmap.mmap(fp.fileno(), 0)
+        mm.seek(0)
+        fd = mm.read()
+        mode = math.ceil(math.log(len(fd), 2))
+        bitset = BitArray(hex='0')
+        for i in range(mode):
+            bitset.append(BitArray(hex='0'))
+        for i in range(len(fd)):
+            bitset.append(fd[i])
+        mm.seek(0)
+        mm.write(bitset)
+
+
+if __name__ == "__
