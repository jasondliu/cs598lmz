import select
# Test select.select()

# We use a unix socket instead of a TCP socket because
# it's easier to setup.

# This is the server. It works in a similar way to the
# client but we bind to a socket and listen for connections
# rather than connecting to a socket.

# Create the server socket
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to a file
file = "/tmp/python_unix_socket_server"

# Make sure the file doesn't already exist
try:
    os.unlink(file)
except OSError:
    if os.path.exists(file):
        raise

server.bind(file)

# Listen for connections
server.listen(5)

# Create an empty list to hold the client sockets
clients = []

# Create a list to hold the data we receive
data = []

# We want to carry on running until we get an explicit
# shutdown command.
while True:

    # We want to check the state of the sockets we're interested
   
