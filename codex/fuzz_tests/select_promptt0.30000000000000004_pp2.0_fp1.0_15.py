import select
# Test select.select()

# Create a pair of connected sockets

if os.name == 'posix':
    # On Unix, sockets are file descriptors
    read_set, write_set, except_set = select.select([sock], [], [], 0)
else:
    # On Windows, sockets are handles
    read_set, write_set, except_set = select.select([sock], [], [], 0)

# If a socket is readable, there is data to read
if sock in read_set:
    data = sock.recv(1024)
    ...

# If a socket is writable, there is buffer space available
if sock in write_set:
    bytes_sent = sock.send(buffer)
    ...

# If a socket is in the exceptional state, there is an error
if sock in except_set:
    ...

# If select() returns three empty lists, the timeout has expired
if not (read_set or write_set or except_set):
    ...

# If select() returns an empty list for one of the three socket groups,
# the corresponding
