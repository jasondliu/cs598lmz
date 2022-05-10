import select
# Test select.select()
# Create two sockets
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind them to two random ports
s1.bind(('', 0))
s2.bind(('', 0))

# Get the port numbers
port1 = s1.getsockname()[1]
port2 = s2.getsockname()[1]

# Connect s2 to s1
s2.connect(('localhost', port1))

# Put s1 and s2 in a list
sockets = [s1, s2]

# Create a new socket s3
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect it to s1
s3.connect(('localhost', port1))

# Put s3 in the list
sockets.append(s3)

# Use select to find the socket(s) that are ready
