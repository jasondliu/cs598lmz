import gc, weakref
+from collections import ChainMap
+from types import MappingProxyType
+from bcc import BPF
+from bcc.utils import printb
+from time import sleep, time
+
+# load BPF program
+b = BPF(src_file="non_map.c")
+
+# functions
+def print_map(print_key=True):
+    print("Hit Count:", b["map"].items())
+
+def read_process(pid):
+    try:
+        comm = open("/proc/%d/comm" % pid, "rb").read()
+    except IOError:
+        comm = b"<...>"
+    return comm.split(b"\0", 1)[0]
+
+# header
+if args.timestamp:
+    print("%-8s" % ("TIME(s)"), end="")
+print("%-16s %-6s %-16s" % ("PCOMM", "PID", "COMM"))
+
+# connect bpf:output to python:input

