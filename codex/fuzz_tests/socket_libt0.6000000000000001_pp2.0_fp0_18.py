import socket
+import sys
+
+import pytest
+
+
+@pytest.fixture(scope='module')
+def client():
+    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    client.connect(('localhost', 12345))
+    yield client
+    client.close()
+
+
+def test_echo(client):
+    message = 'hello'
+    client.sendall(message.encode())
+    recieved = client.recv(1024)
+    assert recieved.decode() == message
+
+
+def test_echo_with_newline(client):
+    message = 'hello\n'
+    client.sendall(message.encode())
+    recieved = client.recv(1024)
+    assert recieved.decode() == message
+
+
+def test_echo_with_multiple_lines(client):
+    message = 'hello\nworld\n'
+    client.sendall(message.encode())
+   
