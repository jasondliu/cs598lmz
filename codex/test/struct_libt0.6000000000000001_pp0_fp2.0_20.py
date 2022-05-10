import _struct
import _os

# Create a socket object
s = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)

# Get local machine name
host = _socket.gethostname()

# Reserve a port for your service.
port = 9999

# Bind to the port
s.bind((host, port))

# Now wait for client connection.
s.listen(5)

while True:
    # Establish connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()
