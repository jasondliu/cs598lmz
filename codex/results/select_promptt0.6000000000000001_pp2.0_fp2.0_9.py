import select
# Test select.select([socket],[socket],[socket])
print('Testing select')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
sock.listen(1)
port = sock.getsockname()[1]

# Accept a connection
# select.select([socket],[socket],[socket],timeout)
# timeout == None -> block until event occurs
# timeout == 0 -> don't block
# timeout > 0 -> block for timeout seconds
print('Waiting for connection...')
r, w, e = select.select([sock], [], [], None)
print('Accepting connection')
conn, addr = sock.accept()
print('Connected to', addr)

# Receive data
print('Waiting to receive data...')
r, w, e = select.select([conn], [], [], None)
data = conn.recv(1024)
print('Received', data.decode('utf8'))

# Send data
print('Sending data...')
r, w, e = select.select
