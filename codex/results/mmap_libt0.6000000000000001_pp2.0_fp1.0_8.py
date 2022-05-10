import mmap
+
+
+def main():
+    """
+    Main method.
+
+    :return: None
+    """
+    with open('lorem.txt', 'r') as f:
+        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
+            print('First 10 bytes via read :', m.read(10))
+            print('First 10 bytes via slice:', m[:10])
+            print('2nd   10 bytes via read :', m.read(10))
+
+
+if __name__ == '__main__':
+    main()

