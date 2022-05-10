import sys, threading

def run():
	# Check Input
	if len(sys.argv) != 5:
		print "Usage: python client.py <host> <port> <username> <password>"
		return
	host = sys.argv[1]
	port = int(sys.argv[2])
	username = sys.argv[3]
	password = sys.argv[4]

	# Create Connection
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	# Send Authentication Data
	authData = username + " " + password + "\r\n"
	s.send(authData)

	# Read Login Status
	loginStatus = s.recv(1024)
	if loginStatus != "Login Successful\r\n":
		print loginStatus
		s.close()
		return

	# Read all messages in current chat
	chatContent = s.recv(1024)
	print chatContent

	# Define Recv Thread Function
	def recvThread():
		
