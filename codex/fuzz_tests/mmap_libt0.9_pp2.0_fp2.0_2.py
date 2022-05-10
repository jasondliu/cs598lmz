import mmap
+
+with open("inp.txt", "rb") as f:
+    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+for i in xrange(10):
+    buf = ""
+    ll = ord(m[i])
+    for j in xrange(i*10,i*10+ll):
+        buf += m[j]
+    if buf:
+        print buf.decode('ascii')
+
+#~ buf = ""
+#~ with open("inp.txt", "rb") as f:
+    #~ while True:
+        #~ b = f.read(1)
+        #~ if not b:
+            #~ break
+            #~ if ord(b) == 1:
+            #~ print buf
+            #~ buf = ""
+        #~ else:
+            #~ buf += b

