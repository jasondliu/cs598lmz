import socket
socket.if_indextoname(1)

#Now, you can use the above IP to connect with the socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((str(IP), 80))
s.listen()


conn, addr = s.accept()
print("Connected to: ", addr[0])

msg = conn.recv(1024)
print("Received: ", msg.decode())

conn.send(b"Hello there!\n")
conn.close()
s.close()
