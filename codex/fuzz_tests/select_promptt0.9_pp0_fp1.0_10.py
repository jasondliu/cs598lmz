import select
# Test select.select in Python
# Source: https://pymotw.com/2/select/

import socket
import select

# Create a socket to connect to the server via sockets
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("localhost", 10000))

while True:
	command = raw_input("Enter a command: ")
	
	# If EOT is entered by the user, then exit the program
	if (command == "EOT"):
		print("Exiting program...")
		client.send("EOT")
		break
	
	# Else, send the command
	client.send(command)
	
	# Add the client to the read list.
	# This read list holds the list of all open socket connections to the server.
	all_read_socks, _, _ = select.select([client], [], []) # _ means we ignore these parameters
	for sock in all_read_socks:
		# Read reply from server by receiving up to 1024 bytes
		response = sock
