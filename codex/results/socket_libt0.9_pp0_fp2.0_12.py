import socket
+from http.server import SimpleHTTPRequestHandler
+from socketserver import TCPServer
+from threading import Thread
+
+def serve(with_page=True):
+    address = ('127.0.0.1', 0)
+    server = TCPServer(address, SimpleHTTPRequestHandler)
+    ip, port = server.server_address
+    print(ip)
+    print(port)
+
+    thread = Thread(target=server.serve_forever)
+    thread.daemon = True  # Don't hang on exit
+    thread.start()
+
+    if with_page:
+        print("Trying to open http://{}:{}".format(ip, port))
+        xdg_open("http://{}:{}".format(ip, port))
+    return ip, port
+
+if __name__ == "__main__":
+    serve(True)

