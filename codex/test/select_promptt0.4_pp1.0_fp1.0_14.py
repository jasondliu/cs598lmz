import select
# Test select.select()

# Create non-blocking sockets
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.setblocking(0)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.setblocking(0)

# Connect to server
s1.connect(('localhost', 9999))
s2.connect(('localhost', 9999))

# Wait for connections to complete
while True:
    try:
        s1.recv(1024)
        s2.recv(1024)
    except socket.error:
        pass
    else:
        break

# Send data to server
s1.send(b'hello')
s2.send(b'world')

# Wait for data to be received
while True:
    try:
        r, w, e = select.select([s1, s2], [], [])
    except socket.error:
        pass
    else:
        break

# Display results
print(r)

# Close sockets

