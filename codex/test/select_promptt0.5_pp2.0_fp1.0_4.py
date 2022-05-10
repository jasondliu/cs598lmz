import select
# Test select.select()
# select.select() is used to monitor multiple file descriptors and wait until one or more of the file descriptors is ready for some kind of I/O operation.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind(('127.0.0.1', 0))
s.listen(1)

# Get the port number.
port = s.getsockname()[1]

# Start a thread with a client that connects to the server.
def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('127.0.0.1', port))

threading.Thread(target=client).start()

# Wait until the client is connected.
while True:
    r, w, e = select.select([s], [], [], 1.0)
    if s in r:
        break

# Accept the connection.
conn, addr = s.accept()

# Close the listening socket.
s
