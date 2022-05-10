import selectors
import socket

# 创建selctor对象
sel = selectors.DefaultSelector()

# 创建socket
sock = socket.socket()
sock.bind(('localhost', 9000))
sock.listen()
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, data=None)


def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1000)
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


while True:
    events = sel.select()
