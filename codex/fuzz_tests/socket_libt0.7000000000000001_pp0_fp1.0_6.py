import socket
+import sys
+
+import requests
+import threading
+
+
+def read_chunk(socket_, size):
+    data = ''
+    while len(data) < size and socket_.connected:
+        new_data = socket_.recv(size - len(data))
+        if not new_data:
+            break
+        data += new_data
+    return data
+
+
+def request_to_dict(request):
+    request_dict = {}
+    key = None
+    request_lines = request.split('\r\n')
+    for line in request_lines[1:]:
+        if line:
+            if line[0] == ' ' or line[0] == '\t':
+                request_dict[key] += line
+            else:
+                key, value = line.split(':')
+                request_dict[key] = value
+    first_line = request_lines[0]
+    method, uri, protocol = first_line.split()
+    ur
