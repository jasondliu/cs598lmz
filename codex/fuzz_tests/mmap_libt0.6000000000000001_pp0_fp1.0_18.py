import mmap
+import os
+import re
+import sys
+
+
+def create_regex(pattern):
+    pattern = re.sub('\s+', '\\s+', pattern)
+    pattern = pattern.strip()
+    return re.compile(pattern)
+
+def print_match(pattern, fname):
+    regex = create_regex(pattern)
+    with open(fname, 'r') as f:
+        for line in f:
+            if regex.search(line):
+                print line
+
+def main():
+    if len(sys.argv) != 3:
+        print "Usage: search_file pattern file"
+        return 1
+    print_match(sys.argv[1], sys.argv[2])
+    return 0
+
+if __name__ == '__main__':
+    sys.exit(main())

