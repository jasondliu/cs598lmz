import socket
+import ssl
+
+server = 'www.python.org'
+port = 443
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.connect((server, port))
+
+cnx = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
+
+print (repr(cnx.getpeername()))
+print (cnx.cipher())
+print (cnx.compression())
+#print (cnx.compression_algorithm)
+print (cnx.version())
+
+cnx.write(b"GET / HTTP/1.0\n\n")
+#print cnx.recv(1024)
+cnx.close()
+

