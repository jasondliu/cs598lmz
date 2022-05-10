import select
# Test select.select()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.listen(5)

# Wait for a connection
readable, writeable, exceptional = select.select([s], [], [])
conn, addr = s.accept()

# Send some data
conn.send(b'hello')

# Wait for the data to be sent
writeable, exceptional = select.select([], [conn], [])

# Close the connection
conn.close()

# Wait for the connection to be closed
readable, exceptional = select.select([conn], [], [])

# Clean up
s.close()

# Test select.poll()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.listen(5)

# Wait for a connection
p = select.poll()
