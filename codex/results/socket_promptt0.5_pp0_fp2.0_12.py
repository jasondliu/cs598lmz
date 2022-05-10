import socket
# Test socket.if_indextoname()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind to the port
s.bind((host, port))

# Now wait for client connection.
s.listen(5)

while True:
   # Establish connection with client.
   c, addr = s.accept()
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()
