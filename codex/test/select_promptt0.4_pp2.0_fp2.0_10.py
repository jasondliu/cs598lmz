import select
# Test select.select()
# select.select() is a blocking function
# It will block until there is data to read
# or until a timeout occurs
# It returns 3 lists:
# 1. The first list contains sockets with data to read
# 2. The second list contains sockets that are ready to send data
# 3. The third list contains sockets that have an error

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Wait for a connection
print('waiting for a connection')
connection, client_address = sock.accept()
print('connection from', client_address)

