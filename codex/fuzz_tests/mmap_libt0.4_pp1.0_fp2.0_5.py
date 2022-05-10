import mmap
+
+
+def main():
+    with open('data.txt', 'r') as f:
+        m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+        print(m.readline())
+        print(m.readline())
+
+
+if __name__ == '__main__':
+    main()

