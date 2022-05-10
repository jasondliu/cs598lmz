import mmap
+import sys
+
+
+vector_len = 64
+
+
+def load_vectors(filename):
+    print("Loading vectors...")
+    with open(filename, "r+b") as f:
+        mm = mmap.mmap(f.fileno(), 0)
+        for i in range(0, mm.size(), vector_len):
+            yield mm[i:i+vector_len]
+
+
+def main():
+    filename = sys.argv[1]
+    for v in load_vectors(filename):
+        print(v)
+
+
+if __name__ == "__main__":
+    main()

