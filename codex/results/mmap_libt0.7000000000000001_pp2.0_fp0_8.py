import mmap
+
+def test_mmap():
+    with open('lorem.txt', 'r') as f:
+        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
+            print('First 10 bytes via read :', m.read(10))
+            print('First 10 bytes via slice:', m[:10])
+            print('2nd   10 bytes via read :', m.read(10))
+
+
+# test_mmap()
+
+
+def test_numpy_mmap():
+    a = np.load('a.npy', mmap_mode='r')
+    print(a)
+    print(a.shape)
+
+
+test_numpy_mmap()

