import mmap
+import os
+import sys
+
+def main():
+    if len(sys.argv) != 2:
+        print("Usage: %s <file>" % sys.argv[0])
+        sys.exit(1)
+
+    filename = sys.argv[1]
+    if not os.path.isfile(filename):
+        print("File %s does not exist" % filename)
+        sys.exit(1)
+
+    f = open(filename, "rb")
+    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+    # Read the header
+    header = m.read(16)
+    magic, version, n_entries, n_bytes = struct.unpack("<4sIIQ", header)
+    if magic != b"\x1f\x8b\x08\x08":
+        print("File %s is not a valid gzipped file" % filename)
+        sys.exit(1)
+
