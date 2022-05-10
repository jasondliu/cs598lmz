import select
# Test select.select()

# Create a new server socket 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', 2222))
serverSocket.listen(5)

# Create a new client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', 2222))

# Create a new socket for the standard input 
inputSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inputSocket.connect(('localhost', 2222))

input = [clientSocket, inputSocket, serverSocket]

# Use select.select() to block until any of the open sockets can be read
inputReady, outputReady, exceptReady = select.select(input, [], [])

