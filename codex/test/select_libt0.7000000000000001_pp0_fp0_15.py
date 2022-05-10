import selectors
import sys

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()
    conn.setblocking(False)
    #
    sel.register(conn, selectors.EVENT_READ, read_data)
    print ("accepted", conn, "from", addr)

def read_data(conn, mask):
    #
    raw_data = conn.recv(1000)
    if raw_data:
        print ("echoing", repr(raw_data), "to", conn)
        conn.send(raw_data)
    else:
        print ("closing", conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, accept)

