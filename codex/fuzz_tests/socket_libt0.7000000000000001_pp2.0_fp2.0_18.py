import socket
+
+# In[2]:
+
+
+s = socket.socket()
+host = socket.gethostname()
+port = 12348
+s.bind((host,port))
+s.listen(5)
+while True:
+    c, addr = s.accept()
+    print("Got connection from",addr)
+    print("Connection from {0} has been established.".format(addr[0]))
+    c.send("Thank you for connecting".encode())
+    c.close()
+
+
+# In[ ]:
+
+
+
+
+
+# In[ ]:
+
+
+
+

