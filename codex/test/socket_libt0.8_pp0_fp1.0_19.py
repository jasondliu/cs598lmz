import socket,time

# start = time.time()
# for i in range(1000):
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect(('127.0.0.1',8081))
# end = time.time()
# print(end - start)

#
# start = time.time()
# for i in range(1000):
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect(('127.0.0.1',8081))
#     s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n')
#     s.recv(1024)
#     s.close()
# end = time.time()
# print(end - start)

start = time.time()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
