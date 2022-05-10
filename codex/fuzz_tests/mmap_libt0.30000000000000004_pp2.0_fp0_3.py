import mmap
+import os
+import re
+import sys
+import time
+
+
+def main():
+    if len(sys.argv) != 2:
+        print("Usage: {} <pid>".format(sys.argv[0]))
+        sys.exit(1)
+
+    pid = int(sys.argv[1])
+    print("pid: {}".format(pid))
+
+    # Open the maps and mem files
+    maps_file = open("/proc/{}/maps".format(pid), "r")
+    mem_file = open("/proc/{}/mem".format(pid), "rb")
+
+    # Create a regex that matches the line we're looking for
+    pattern = re.compile(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])')
+
+    # Iterate over each line in the maps file
+    for line in maps_file:
+        match = pattern.match(line)
+
+
