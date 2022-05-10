import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

ans = True
while(ans):
    s.sendall(b"ping\n")
    time.sleep(1)
    data = s.recv(1024)
    if len(data) != 0:
        print(str(data))

s.close()
