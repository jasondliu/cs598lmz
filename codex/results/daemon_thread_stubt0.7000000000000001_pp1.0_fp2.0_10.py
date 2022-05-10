import sys, threading

def run():
	# you can change the default port number here, if you want to
	server_socket = socket(AF_INET, SOCK_STREAM)
	server_socket.bind(('', 12345))
	server_socket.listen(5)
	while True:
		# TODO: Write code here to handle connection from a client
		print("server waits for connection...")
		connection_socket, addr = server_socket.accept()
		print("server connected with client : ",addr)
		threading._start_new_thread(client_thread, (connection_socket,))

def client_thread(connection_socket):
	message = ''
	while True:
		# TODO: Write code here to handle communication with a client
		message = connection_socket.recv(2048).decode()
		if message != "exit":
			print("client message: ", message)
		else:
			break
		response = message.upper()
		connection_socket.send(response.encode())
	connection_socket.
