import selectors
import sys
import types

# Create a TCP/IP socket
server_address = ('localhost', 10000)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

# Create a selector object
sel = selectors.DefaultSelector()

# Register the server socket
sel.register(server, selectors.EVENT_READ, data=None)

# Function to accept a connection
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

# Function to read data
def service_connection(key, mask):
    sock = key.file
