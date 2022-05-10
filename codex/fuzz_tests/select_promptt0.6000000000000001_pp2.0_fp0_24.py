import select
# Test select.select()

# Create a pair of connected sockets
if os.name == 'posix':
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sockname = 'pysocket-test'
    try:
        os.unlink(sockname)
    except OSError:
        if os.path.exists(sockname):
            raise
else:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockname = (HOST, PORT)

server.bind(sockname)
server.listen(1)

# Connect the client to the server
client.connect(sockname)

# Set up the poller
poller = select.poll()
poller.register(client, select.POLLIN)

# Poll for activity
if poller
