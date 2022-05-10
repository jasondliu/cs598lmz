import socket
socket.if_indextoname(4)

print("Received data")

for p in packet:
        print(p,end='')
