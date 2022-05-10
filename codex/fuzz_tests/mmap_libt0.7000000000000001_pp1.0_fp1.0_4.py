import mmap
+
+# Open a file
+f = open('lorem.txt', 'r+')
+
+# Memory-map the file, size 0 means whole file
+mm = mmap.mmap(f.fileno(), 0)
+
+# Read content via standard file methods
+print(mm.readline())  # prints "Hello Python!"
+
+# Update content using file's write method.
+mm.seek(0)  # rewind
+mm.write(b'Hello World!')
+
+# ... and read again using standard file methods.
+mm.seek(0)
+print(mm.readline())
+
+f.close()

