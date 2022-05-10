import select
# Test select.select can handle a long time to return.
# See 'Issue#18526: select.select is not interruptible'
import socket

def echo_server(port):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', port))
    server.listen(1)
    while True:
        conn, addr = server.accept()
        msg = conn.recv(1024)
        conn.sendall(msg)
        conn.close()


import threading

server = threading.Thread(target=echo_server, args=(0,))
server.start()
port = server.get_ident()


# Blocking test: client -> server
client = socket.socket()
client.connect(('127.0.0.1', port))

client.sendall(b'a')
s,o,e = select.select([client], [], [], 2)
client.close()
assert s


# Time-
