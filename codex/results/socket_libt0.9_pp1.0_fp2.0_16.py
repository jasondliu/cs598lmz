import socket
+import time
+import threading
+from sr1 import SR1
+
+
+"""
+Communication class is responsible for sending and receiving messages to/from the STM32 board. 
+The Micro-controller MUST have MD5 server protocol enabled in order to support this class. See the MD5 protocol manual,
+link below.
+
+@author:     Juan Camilo Villa
+@copyright:  2014.  All rights reserved.
+@license:    license
+@contact:    jcvillarre@gmail.com
+@deffield    updated: Updated
+"""
+        
+__all__ = []
+__version__ = 0.1
+__date__ = '2014-07-11'
+__updated__ = '2014-07-11'
+
+def communication_thread(ip, port, communication):
+        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
+
+        while 1:
+                data, addr = sock.recvfrom(1024)
+                if len(data) > 0
