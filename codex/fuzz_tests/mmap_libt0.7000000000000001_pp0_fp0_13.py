import mmap
+
+
+def main():
+    # Open a file for both reading and writing
+    f = open("hello.txt", "r+b")
+
+    # Memory-map the file, size 0 means whole file
+    mm = mmap.mmap(f.fileno(), 0)
+
+    # Read content via standard file methods
+    print("Before:")
+    print(repr(mm.readline()))
+
+    # # Move to the beginning of the file
+    mm.seek(0)
+
+    # Read the entire file
+    print(repr(mm.readline()))
+
+    # # Move to the beginning of the file
+    mm.seek(0)
+
+    # # Write to the file
+    mm.write(b"World!")
+
+    # # Move to the beginning of the file
+    mm.seek(0)
+
+    # # Read the entire file
+    print("After:")
+    print(repr(mm.readline()))
