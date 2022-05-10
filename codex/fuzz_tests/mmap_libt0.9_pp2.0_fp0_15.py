import mmap
+
+
+def read_mem_info():
+    with open("/proc/meminfo", "rb") as f:
+        return mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
+
+
+def parse_mem_info(mem_info):
+    lines = mem_info.split("\n")
+    mem_dict = {}
+    for line in lines:
+        key, val = line.split(": ")
+        mem_dict[key.lower()] = val
+    return mem_dict
+
+
+def parse_free_mem(mem_dict):
+    free_mem = re.compile("memfree")
+    total_buff_cache = re.compile("buffers\|cached")
+
+    free_mem_total = sum(int(mem_dict[field]) for field in mem_dict if free_mem.search(field))
+    buff_cache_total = sum(int(mem_dict[field]) for field in mem_dict if
