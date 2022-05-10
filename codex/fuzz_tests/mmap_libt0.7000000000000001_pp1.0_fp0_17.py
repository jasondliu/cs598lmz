import mmap
+
+def main():
+    # Open a file
+    f = open('lorem.txt', 'r+')
+
+    # Create a memory map (mmap)
+    #mm = mmap.mmap(f.fileno(), 0)
+    #mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
+
+    # Read content via standard file methods
+    print(f.readline())
+
+    # Read content via slice notation
+    print(mm[:10])
+
+    # Update content using slice notation;
+    # note that new content must have same size
+    mm[6:9] = b'xyz'
+
+    # ... and read again using standard file methods
+    f.seek(0)
+    print(f.readline())
+
+    # Close the open file
+    f.close()
+
