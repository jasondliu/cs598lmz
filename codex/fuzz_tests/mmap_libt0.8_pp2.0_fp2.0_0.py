import mmap
+
+def main():
+    with open('lorem.txt', 'r') as f:
+        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
+            print('First 10 bytes via read :', m.read(10))
+            print('First 10 bytes via slice:', m[:10])
+            print('Last 10 via read :', m.read(10))
+            print('Last 10 via slice:', m[-10:])
+            print('Slice copy via read:', m.read(10))
+            m.seek(0)
+            print('First 10 bytes via read :', m.read(10))
+            print('First 10 bytes via slice:', m[:10])
+            print('Last 10 via read :', m.read(10))
+            print('Last 10 via slice:', m[-10:])
+
+if __name__ == '__main__':
+    main()

