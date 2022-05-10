import select
# Test select.select

# Create a pair of connected sockets
s1, s2 = socket.socketpair()

# Add them to the selectable set
rlist = [s1, s2]

# Send some data from s1
s1.send(b'hello')

# Wait for a response
readable, writable, exceptional = select.select(rlist, [], [])

# Read the response
print(readable)
print(s2.recv(1024))
