import mmap
+
+
+# Open the file as binary data
+f = open('/dev/vboxdrv', "r+b")
+
+# Memory-map the file, size 0 means whole file
+mm = mmap.mmap(f.fileno(), 0)
+
+# Read contents...
+print mm.readline()  # prints "Hello Python!"
+
+# ...and write the same data back
+mm.seek(0)    # rewind
+mm.write("Hello Python!\n")
+mm.flush()
+
+# Close the map and file
+mm.close()
+f.close()

