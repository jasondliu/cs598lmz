import selectors
import time

host = '127.0.0.1'
port = 65432

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print('Accepted connection from ', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    if data:
        print('Echoing ', repr(data), 'to ', conn)
        conn.send(data)
    else:
        print('Closing connection to ', conn)
        sel.unregister(conn)
        conn.close()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on ', (host, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, accept)

