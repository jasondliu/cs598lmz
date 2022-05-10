import select, socket
+from threading import Thread, Event, Lock
+
+
+class Server:
+    def __init__(self, addr):
+        self.addr = addr
+        self.death_event = Event()
+
+        self.socket = self._get_socket(self.addr)
+        self.epoll = select.epoll()
+        self.epoll.register(self.socket.fileno(), select.EPOLLIN)
+
+        self.listen()
+
+    def _get_socket(self, addr):
+        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+        sock.setblocking(0)
+        sock.bind(addr)
+        sock.listen(10)
+        return sock
+
+    def listen(self):
+        while True:
+            events = self.epoll.poll(1)
+            for
