import mmap
+
+
+def main():
+    filename = 'test.txt'
+
+    print("Memory-map %r" % filename)
+    f = open(filename, 'w+')
+    f.write('012345678abcdef\n')
+    f.write('012345678abcdef\n')
+
+    f.seek(0)
+    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+    # Read content via standard file methods
+    print("File:")
+    print(f.readline().rstrip())
+    print(f.readline().rstrip())
+
+    # Read content via memory-mapping
+    print("Memory:")
+    print(m.readline().rstrip())
+    print(m.readline().rstrip())
+
+    # Update content using slice notation;
+    # note that new content must have same size
+    m[6:11] = 'WORLD'
+    m.
