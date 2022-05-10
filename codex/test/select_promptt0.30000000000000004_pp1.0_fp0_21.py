import select
# Test select.select()

# Create two sockets
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind them to something
sock1.bind(('localhost', 8001))
sock2.bind(('localhost', 8002))

# Listen for connections
sock1.listen(5)
sock2.listen(5)

# Create a list of sockets that we want to check for readability
read_list = [sock1, sock2]

# Create a list of sockets that we want to check for writability
write_list = []

# Create a list of sockets that we want to check for errors
error_list = []

# Select will return three lists of sockets that are ready for reading, writing, and errors
