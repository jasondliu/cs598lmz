import select
# Test select.select
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

sock.sendall(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')

r, w, x = select.select([sock], [], [])

if sock in r:
    data = sock.recv(4096)
    print(data)
</code>

