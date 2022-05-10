import socket
import select

# Function to broadcast chat messages to all connected clients
def broadcast_data(sock, message):
	# Do not send the message to master socket and the client who has send us the message
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != sock:
			try:
				socket.send(message)
			except:
				# broken socket connection may be, chat client pressed ctrl+c for example
				socket.close()
				CONNECTION_LIST.remove(socket)

if __name__ == "__main__":
	# List to keep track of socket descriptors
	CONNECTION_LIST = []
	RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
	PORT = 5000
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# this has no effect, why ?
