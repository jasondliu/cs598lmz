import select
# Test select.select()
# Select takes 3 parameters.
# 1. All readable sockets
# 2. All writeable sockets
# 3. All error sockets
# If we want to wait for all 3, we just pass 3 identical arrays.
# select() will return the sockets that it is ready to read from as well as sockets that are ready to write to.
readable, writeable, error = select.select([sock,], [sock,], [sock,])

# Read from the socket if readable
if readable:
    print(sock.recv(1024))

# Write to the socket if writeable
if writeable:
    sock.send("Hello Server")

# Check for errors in the socket
if error:
    print(error)
