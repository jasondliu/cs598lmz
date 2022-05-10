import select
# Test select.select()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Pass them to select()

r, w, e = select.select( [sock1], [sock2], [] )

# Sockets are ready for reading

print 'ready for reading:', r

# Sockets are ready for writing

print 'ready for writing:', w

# No sockets have errors

print 'with errors:', e

# Close sockets

sock1.close()
sock2.close()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Pass them to select()

r, w, e = select.select( [sock1], [sock2], [] )

# Sockets are ready for reading

print 'ready for reading:', r

# Sockets are ready for writing

print 'ready for writing:', w

# No sockets have errors


