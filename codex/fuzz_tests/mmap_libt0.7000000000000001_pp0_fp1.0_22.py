import mmap
+
+
+def main():
+    with open("/home/siddharth/Downloads/iphone6_64.img", "rb") as f:
+        mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+        pos = 0
+        while 1:
+            m = mm.read(2)
+            if m == b"":
+                break
+            print(m)
+            pos += 1
+
+        mm.close()
+
+
+if __name__ == '__main__':
+    main()

