import socket 
+
+s = socket.socket()           
+print('Socket successfully created')
+
+port = 12345                
+s.bind(('0.0.0.0', port))         
+print('socket binded to %s' %(port)) 
+s.listen(5)      
+print("socket is listening")            
+
+while True: 
+    c,addr = s.accept()      
+    print('Connected to :', addr[0], ':', addr[1]) 
+    print("Enter the data")
+    data=input()
+    c.send(data.encode())
+    c.close() 
+
+
+
+
+
+
+
+
+
+
+
+
+
+
+

