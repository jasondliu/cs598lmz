import selectors
import socket
import types

# The client socket must be connected to the server
# before the server can receive messages from the client.

sel = selectors.DefaultSelector()

def accept_wrapper(sock):
    conn, addr = sock.accept() # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    message = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=message)

def service_connection(key, mask):
    sock = key.fileobj
    message = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024) # Should be ready to read
        if recv_data:
            print('received', repr(recv_data), 'from connection', message.addr)
            message.outb += recv_data
        else:
            print
