import mmap
+
+
+def get_regex_dict(filename):
+    regex_dict = {}
+    with open(filename, 'r') as f:
+        for line in f.readlines():
+            if line.startswith('#'):
+                continue
+            line = line.strip()
+            if len(line) < 1:
+                continue
+            regex_dict[line] = re.compile(line)
+    return regex_dict
+
+
+def main():
+    if len(sys.argv) < 4:
+        print('Usage: {0} <file> <regex-file> <output>'.format(sys.argv[0]))
+        return
+
+    regex_dict = get_regex_dict(sys.argv[2])
+    mm = mmap.mmap(sys.argv[1], 0, access=mmap.ACCESS_READ)
+    out = open(sys.argv[3], 'w')
+
+    for regex in regex_dict
