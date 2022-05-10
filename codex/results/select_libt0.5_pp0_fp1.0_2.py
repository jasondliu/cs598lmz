import select
+import socket
+import sys
+import time
+import traceback
+
+
+def main():
+    start_server()
+
+
+def start_server():
+    host = ''
+    port = 5555
+    backlog = 5
+    size = 1024
+    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    server.bind((host, port))
+    server.listen(backlog)
+    input = [server, sys.stdin]
+    running = 1
+    while running:
+        inputready, outputready, exceptready = select.select(input, [], [])
+
+        for s in inputready:
+            if s == server:
+                client, address = server.accept()
+                input.append(client)
+                print "Client connected:", address
+            elif s == sys.stdin:
+                junk = sys.stdin.readline()
+                running = 0
+            else:
+                try:
+                   
