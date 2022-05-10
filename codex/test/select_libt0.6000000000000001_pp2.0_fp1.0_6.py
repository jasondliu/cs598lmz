import selectors

# 连接池
sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    print("accepting", conn, "from", addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1000)
    if data:
        print("echoing", repr(data), "to", conn)
        conn.send(data)
    else:
        print("closing", conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(("localhost", 1234))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
