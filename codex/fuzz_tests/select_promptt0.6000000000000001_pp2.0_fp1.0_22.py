import select
# Test select.select

def read_input(stream):
	# Read data from the given stream until a newline character is encountered.
	data = stream.readline()
	return data

def server():
	# Create a TCP/IP socket.
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Set the socket to be reusable.
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# Bind the socket to the port.
	server_address = ('localhost', 10000)
	print('starting up on %s port %s' % server_address)
	sock.bind(server_address)
	# Listen for incoming connections.
	sock.listen(1)

	while True:
		# Wait for a connection.
		print('waiting for a connection')
		connection, client_address = sock.accept()
		try:
			print('connection from', client_address)
			# Read data from the connection.
		
