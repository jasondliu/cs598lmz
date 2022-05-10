import socket
+
+s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+s.connect(('localhost', 50000))
+message = raw_input("Enter command: ")
+s.send(message)
+s.close()

