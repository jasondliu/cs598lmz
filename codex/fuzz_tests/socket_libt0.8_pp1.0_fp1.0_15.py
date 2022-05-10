import socket
+import subprocess
+import sys
+
+
+if __name__ == "__main__":
+    if len(sys.argv) < 2:
+        print("Usage: ./pinger.py <host> [<n>]")
+        exit(-1)
+
+    host = sys.argv[1]
+    n = 1
+    if len(sys.argv) > 2:
+        n = int(sys.argv[2])
+
+    for i in range(n):
+        print("Pinging {}...".format(host))
+
+        response = subprocess.run(["ping", "-c", "1", host],
+                                  stdout=subprocess.PIPE,
+                                  stderr=subprocess.PIPE,
+                                  universal_newlines=True)
+
+        response = response.stdout.split("\n")
+        if "0 received" in response[-2]:
+            print("{} failed to respond".format(host))
+        else:

