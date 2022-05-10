import select
# Test select.select()

def accept(sock, mask):
    new_connection, addr = sock.accept()
    print('accepted', addr)
    new_connection.setblocking(False)
    sel.register(new_connection, select.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)

sel = select.epoll()
sel.register(sock, select.EVENT_READ, accept)

while True:
    events = sel.poll()
