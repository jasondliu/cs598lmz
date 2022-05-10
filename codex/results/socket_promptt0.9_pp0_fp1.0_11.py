import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(10))

# Restart connection after a socket error
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

try:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.sendall(b'Hi, there.')
    c.close()
except (Exception, KeyboardInterrupt):
    s.close()
    print('Closed.')

# Wrap socket object with a file-like object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

try:
    c, addr = s.accept()
    print('Got connection from', addr)
    f = c.makefile('rw')
    f.write(b'Hi, there
