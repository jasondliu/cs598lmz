import socket, select, string, sys

def prompt() :
	sys.stdout.write('You > ')
	sys.stdout.flush()

#main function

if __name__ == "__main__":

	if (len(sys.argv) < 2) :
		print('Usage: python client.py hostname')
		sys.exit()
	host = sys.argv[1]
	port = 5000

	#create a list of sockets from conf file

	try :
		#establish socket
		s = socket.socket(socket.AF_INET, so
