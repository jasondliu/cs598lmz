import select
# Test select.select()
#
# Usage: python select-test.py
#
# This script runs a simple echo server that listens on a TCP port.
# It accepts multiple connections and echos back whatever is sent.
#
# The script uses select.select() to determine which sockets are readable.
#
# The server is single threaded.  If a client is slow to respond, the server
# will not be able to service other clients.

PORT = 12345

def main():
	# create a TCP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# bind the socket to the port
	server_address = ('localhost', PORT)
	print('starting up on %s port %s' % server_address)
	sock.bind(server_address)

	# listen for incoming connections (server mode) with 5 max connection
	sock.listen(5)

	# list of connections
	connections = [sock]

	while True:
		print('\nwaiting for a connection')
		readable, writable, exceptional
