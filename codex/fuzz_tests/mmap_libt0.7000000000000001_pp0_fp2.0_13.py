import mmap
+
+# Open a file
+f = open("./file.txt", "wb")
+
+# Write to the file
+f.write(b"Hello Python!\n")
+
+# Close the file
+f.close()
+
+# Open the file again
+f = open("./file.txt", "r+")
+
+# Create a memory map
+m = mmap.mmap(f.fileno(), 0)
+
+# Read from the memory map
+print(m.readline())
+
+# Close the map
+m.close()
+
+# Close the file
+f.close()
+
+
+
+
+

