import socket
+s = socket.socket()
+s.bind(("",8000))
+s.listen(1)
+print("Waiting for client...")
+conn, addr = s.accept()
+print("Connected with " + addr[0] + ":" + str(addr[1]))
+file = open("lorem.txt","rb")
+l = file.read(1024)
+while (l):
+    conn.send(l)
+    print("Sent ",repr(l))
+    l = file.read(1024)
+file.close()
+print("finished sending")
+conn.send("finished sending".encode('ascii'))
+conn.close()

