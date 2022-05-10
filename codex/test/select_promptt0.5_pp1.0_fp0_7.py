import select
# Test select.select()
# select() can monitors multiple sockets for data arrival
# and returns a list of sockets that are ready for reading

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket to be non-blocking
s.setblocking(0)

# Connect to the server
s.connect(("www.baidu.com", 80))

# Create a file object from the socket
f = s.makefile("rw")

# Send a request to the server
f.write("GET / HTTP/1.0\n\n")

# Read the response
response = f.read()
