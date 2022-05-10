import select
# Test select.select
import os, socket, sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(10)

inputs = [server]
outputs = []

while True:
	readable, writable, exceptional = select.select(inputs, [], [], 1)
	for socket in readable:
		if socket is server:
			client, address = socket.accept()
			client.setblocking(0)
			inputs.append(client)
		else:
			data = socket.recv(1024)
			if data:
				outputs.append(socket)
			else:
				inputs.remove(socket)
				socket.close()

	for socket in writable:
		socket.send('hello')
		outputs.remove(socket)
