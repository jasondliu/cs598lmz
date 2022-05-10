import socket
import sys

peer = sys.argv[2]
port = int(sys.argv[1])
s = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
s1 = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
s2 = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
s3 = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
s.bind(('', port))
s.listen(5)
s1.connect((peer, port))
s3.connect((peer, port))

#send file name
filename = sys.argv[3]
string = "SEND " + filename + "\n\n"
s1.sendall(string.encode("utf-8"))
reply = s1.recv(1024)
print("Phase1: File request accepted by the server.")

#open file and prepare info
