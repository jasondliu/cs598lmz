import signal
signal.signal(signal.SIGINT, signal_handler)

# IP address of the server
HOST = "127.0.0.1"

# the number of PORT the server is listening for
PORT = 5005

# the address of the server
ADDR = (HOST, PORT)

# connection to the server
server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDR)

# I add a number to the username to identify the client
# it will make the chat easier to follow
name = socket.gethostname() + "_" + str(socket.gethostbyname(socket.gethostname()))
print("Connected to chat server")

