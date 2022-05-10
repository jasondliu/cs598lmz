import select
# Test select.select with a timeout

import select
import socket
import time

def test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    s.setblocking(0)
    port = s.getsockname()[1]
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('localhost', port))
    c.setblocking(0)
    ready = select.select([s], [], [], 0.1)
    if ready[0]:
        conn, addr = s.accept()
        conn.close()
    ready = select.select([c], [], [], 0.1)
    if ready[0]:
        data = c.recv(1024)
        if data:
            c.close()
    s.close()
    c.close()

for i in range(1000):
    test()
