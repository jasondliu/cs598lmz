import selector
import sys
import socket

start = time.clock()
sel = selector.DefaultSelector()
stopped = False


def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    global stopped
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()
        # Tell the main loop to stop
        stopped = True


sock = socket.socket()
sock.bind(('localhost', 3000))
sock.listen(100)
