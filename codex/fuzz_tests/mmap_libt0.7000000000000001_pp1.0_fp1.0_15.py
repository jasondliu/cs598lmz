import mmap
+import sys
+import hashlib
+
+def main(file_to_hash, block_size=2**20):
+    hasher = hashlib.md5()
+    
+    with open(file_to_hash, 'rb') as f:
+        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
+
+        while True:
+            data = mm.read(block_size)
+            if not data:
+                break
+            hasher.update(data)
+
+    return hasher.hexdigest()
+
+if __name__ == '__main__':
+    file_to_hash = sys.argv[1]
+    print(main(file_to_hash))

