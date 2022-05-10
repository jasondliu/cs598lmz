import mmap
+
+
+def main():
+    with open("test.txt", "r+b") as f:
+        mm = mmap.mmap(f.fileno(), 0)
+        print(mm.readline())
+        mm.seek(0)
+        mm.write(b"0123456789abcdef")
+        mm.seek(8)
+        print(mm.read(1))
+        mm.close()
+
+
+if __name__ == "__main__":
+    main()

