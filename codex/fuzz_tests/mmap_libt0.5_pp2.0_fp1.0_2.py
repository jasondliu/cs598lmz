import mmap
+import struct
+import sys
+
+
+def main(argv):
+    if len(argv) != 2:
+        print "Usage: %s <pid>" % argv[0]
+        return -1
+    pid = int(argv[1])
+    with open('/proc/%d/pagemap' % pid, 'rb') as f:
+        m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+        for i in range(0, len(m), 8):
+            entry = struct.unpack('Q', m[i:i+8])[0]
+            page_frame_number = entry & 0x7FFFFFFFFFFFFF
+            print "Page frame number: %s" % page_frame_number
+        m.close()
+    return 0
+
+if __name__ == '__main__':
+    sys.exit(main(sys.argv))

