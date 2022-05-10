import select
# Test select.select()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Pass them to select()

r, w, e = select.select([sock1], [], [])

# Sockets are ready for reading

print 'sock1 is ready for reading'

# Sockets are ready for reading

print 'sock1 is ready for reading'

# Send some data

sock2.send('text')

# Send some data

sock2.send('text')

# Sockets are ready for reading

print 'sock1 is ready for reading'

# Sockets are ready for reading

print 'sock1 is ready for reading'

# Receive some data

print sock1.recv(100)

# Receive some data

print sock1.recv(100)

# Sockets are not ready for reading

print 'sock1 is not ready for reading'

# Sockets
