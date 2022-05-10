import mmap
+import os
+
+with open('lorem.txt', 'r+') as f:
+    with mmap.mmap(f.fileno(), 0) as m:
+        print(len(m))
+        print(m[1:4])
+        m[:4] = b'ABCD'.encode()
+        print(m[:4])
+        m[1:4] = b'EFG'.encode()
+        print(m[:4])
+        m.seek(0)
+        print(m.read(4))
+        m.read(4)
+        m.seek(0)
+        print(m[:4])
+        m.seek(0)
+        print(m.readline())
+        m.seek(0, os.SEEK_END)
+        m.write(b'foo'.encode())
+        m.seek(0, os.SEEK_END)
+        m.write(b'bar'.encode())
+        m.flush()

