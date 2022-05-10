import mmap
+import re
+import os
+
+m = mmap.mmap(0, os.path.getsize(args['filepath']), 'r')
+
+for line in iter(m.readline,''):
+    print line
+
+
+
+
+
+# mmap.ACCESS_READ
+
+# for line in fp:
+#     data = fp.readline()
+#     # print data
+#     line.rstrip()
+#     m = re.search('\[(.*?)\]', line)
+
+#     if m:
+#         match = m.group()
+#         print match
+#     else:
+#         print 'No match'
+#         # (string) or (m.group(1)) or (m.group(2)) or (m.group(3)) or (m.group(4)) or (m.group(5)) or (m.group(6))
+#     # print m
+#     # [rstrip()]
+#     #
