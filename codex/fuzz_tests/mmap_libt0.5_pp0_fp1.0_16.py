import mmap
+
+# Open the file as a binary stream
+f = open('data.txt', 'rb')
+
+# Create a memory-map to the file, size 0 means whole file
+map = mmap.mmap(f.fileno(), 0)
+
+# Read content via standard file methods
+print map.readline()
+
+# Read content via slice notation
+print map[:5]
+
+# Update content using slice notation;
+# note that new content must have same size
+map[6:] = ' world'
+
+# ... and read again using standard file methods
+map.seek(0)
+print map.readline()
+
+# close the map
+map.close()
+
+# close the file
+f.close()

