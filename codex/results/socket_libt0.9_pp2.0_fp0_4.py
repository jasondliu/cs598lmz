import socket
+import json
+import time
+
+
+def pygame_change(x_offset, y_offset, scroll_num):
+    pygame.init()
+    screen = pygame.display.set_mode((300, 300))
+    pygame.display.set_caption('Socket Server')
+
+    done = False
+    try:
+        pygame.mouse.set_pos([pygame.mouse.get_pos()[0] + x_offset, pygame.mouse.get_pos()[1] + y_offset])
+    except:
+        done = True
+    pygame.display.update()
+    time.sleep(0.001)
+
+
+# Create a UDS socket
+sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
+
+# Connect the socket to the port where the server is listening
+server_address = '/tmp/python_unix_socket_server'
+print('connecting to %s' % server_address)
+try:

