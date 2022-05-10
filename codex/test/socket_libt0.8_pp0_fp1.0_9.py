import socket

url  = "http://www.naver.com"
fsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

fsock.connect((url,80))
fsock.send(b"GET / HTTP/1.0\r\n\r\n")
res = fsock.recv(512)

print(res.decode())
