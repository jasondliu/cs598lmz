import mmap
+
+
+def find_char(file, char):
+    with open(file, "r+b") as f:
+        mm = mmap.mmap(f.fileno(), 0)
+        i = mm.find(char)
+        print("POS: ", i)
+        mm.close()
+
+
+if __name__ == "__main__":
+    find_char("test.txt", b"\n")

