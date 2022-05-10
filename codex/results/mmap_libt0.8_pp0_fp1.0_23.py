import mmap
+import re
+import sys
+
+
+def contains(filename, query):
+    haystack = open(filename, 'r')
+
+    with open(filename, 'r') as f:
+        s = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+        if re.search(query, s):
+            print(filename)
+            return True
+
+    return False
+
+def main():
+    if len(sys.argv) < 3:
+        print('Usage: find_text.py <text> <path>')
+        sys.exit(1)
+
+    query = sys.argv[1]
+    path = sys.argv[2]
+
+    for root, dirs, files in os.walk(path):
+        for f in files:
+            if query in f:
+                print(os.path.join(root, f))
+            else:
+                contains(os.path.join(root, f), query
