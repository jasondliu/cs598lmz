import socket
import sys

HOST = ''
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
	sock.bind((HOST, PORT))
except socket.error as msg:
	print ('Bind failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
	sys.exit()

print ('Socket bind complete')
sock.listen(10)
print ('Socket listening now')

conn, addr = sock.accept()
print ('Connected to ' + addr[0] + ':' + str(addr[1]))

while True:
	data = conn.recv(60)
	print(data.decode())
	command = input("Command: ")
	conn.sendall(command.encode())
	data = conn.recv(60)
	print(data.decode())
	if command == "QUIT":
		break

	
conn.close()
sock.close()
