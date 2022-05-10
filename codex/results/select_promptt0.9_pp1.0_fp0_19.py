import select
# Test select.select()

import socket
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

server_address = ('localhost', 10000)
server.bind(server_address)
server.listen(10)

inputs = [server]

outputs = []

message_queues = {}

while inputs:
	readable, writable, exceptional = select.select(
		inputs, outputs, inputs)
	for s in readable:
		if s is server:
			connection, client_address = s.accept( )
			connection.setblocking(False)
			inputs.append(connection)
			message_queues[connection] = Queue.Queue( )
		else:
			data = s.recv(1024)
			if data:
				# A readable client socket has data
				print "received ", data, "from ", s.getpeername()
				message_queues[
