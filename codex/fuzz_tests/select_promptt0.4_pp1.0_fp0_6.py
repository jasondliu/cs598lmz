import select
# Test select.select()

# Make a pair of connected sockets
s1, s2 = socket.socketpair()

# Add them to the selector
sel = select.select([s1], [], [], 0)

# Check if they are ready to read
print(sel)

# Check if they are ready to write
sel = select.select([], [s1], [], 0)
print(sel)

# Check if they have an error
sel = select.select([], [], [s1], 0)
print(sel)

# Send some data
s1.send(b'x')

# Check if they are ready to read
sel = select.select([s2], [], [], 0)
print(sel)

# Check if they are ready to write
sel = select.select([], [s2], [], 0)
print(sel)

# Check if they have an error
sel = select.select([], [], [s2], 0)
print(sel)

# Receive some data
s2.recv(1)

# Check if they are ready to
