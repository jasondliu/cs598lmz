import mmap
+
+
+def parse_file(path):
+    f = open(path, "r+")
+    # memory-map the file, size 0 means whole file
+    map = mmap.mmap(f.fileno(), 0)
+    # read content via standard file methods
+    print("mmap size:", map.size())
+    print("content:", map.readline())
+
+
+if __name__ == "__main__":
+    parse_file("file")

