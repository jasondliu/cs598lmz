import select
import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create an endpoint
host = socket.gethostname()
port = 12345
s.bind((host, port))

# become a server socket
s.listen(5)

# create a list of sockets for select.select()
inputs = [s]

# create a list of sockets for output
outputs = []

# create a dictionary for message queue
message_queues = {}

