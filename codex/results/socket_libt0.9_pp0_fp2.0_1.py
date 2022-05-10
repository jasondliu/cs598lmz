import socket
+
+
+def make_payload(data):
+    output = struct.pack(">BI", 1, len(data))
+    output += data.encode("utf-8")
+    return output
+
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.connect(("127.0.0.1", 8091))
+
+payload = make_payload("hello\n")
+s.send(payload)
+data = s.recv(8192)
+print("recvd:", data)
+
+s.close()

