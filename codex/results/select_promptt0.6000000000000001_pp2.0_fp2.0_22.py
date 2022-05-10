import select
# Test select.select()
def read_socks(socks):
	for sock in socks:
		data = sock.recv(1024)
		if not data:
			print "Disconnected"
			sock.close()
		else:
			print data

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the port
server_address = ('localhost', 10000)
print 'starting up on %s port %s' % server_address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

# Sockets from which we expect to read
inputs = [server_socket]
# Sockets from which we expect to write
outputs = []

sock_to_name = {}

while inputs:
	# Wait for at least one of the sockets to be ready
