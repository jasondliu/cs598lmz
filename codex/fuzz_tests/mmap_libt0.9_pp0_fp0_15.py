import mmap
+import os
+
+def read_worker(queue):
+    f = open("/dev/mem", "rb", buffering=0)
+    mem = mmap.mmap(f.fileno(), 16384, offset=0x8C000000)
+    for byte_index in iter(queue.get, 'STOP'):
+        output_fd.write(mem[byte_index])
+    f.close()
+    mem.close()
+
+def main():
+    output_fd = open("/tmp/memcopy", "wb")
+
+    queue = Queue()
+    for n in range(8):
+        Process(target=read_worker, args=(queue,)).start()
+
+    qindex = 0
+    for byte_index in range(0, 16384):
+        queue.put(byte_index)
+        if qindex > 64:
+            queue.put('STOP')
+            break
+        qindex = qindex + 1
+
+    for n in range(8):
+
