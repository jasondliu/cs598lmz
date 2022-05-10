import selectors
+import socket
+
+HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
+PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
+
+
+# an object that encapsulate a connection.
+class Connection:
+    def __init__(self, sock, selector):
+        self.sock = sock
+        self.selector = selector
+        self._recv_buffer = b''
+        self._send_buffer = b''
+
+        # selector.register는 이 메소드의 리턴 값이다.
+        # EVENT_READ와 EVENT_WRITE는 리스니어블이 이벤트가 걸렸을 때 호출된다.
+        self._selector_key = selector.register(
