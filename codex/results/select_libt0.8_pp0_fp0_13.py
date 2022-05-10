import select
+
+
+class Client:
+    def __init__(self, conn):
+        self.conn = conn
+
+    def receive(self):
+        packets = []
+        while True:
+            packet = recvall(self.conn, 4)
+            if not packet:
+                break
+            length, = struct.unpack("!I", packet)
+            data = recvall(self.conn, length, 1024)
+            if not data:
+                break
+            packets.append(data)
+            if len(packets) >= 50:
+                break
+        return packets
+
+
+def recvall(sock, length, max_buffer=4096):
+    data = b""
+    while len(data) < length:
+        packet = sock.recv(length - len(data))
+        if not packet:
+            return None
+        data += packet
+    return data
+
+
+def main(port):
+    print("Starting up on 0.0.0
