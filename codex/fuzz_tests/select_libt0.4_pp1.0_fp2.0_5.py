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

while inputs:
    # monitor all sockets
    print '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    # when a readable socket is ready
    for r in readable:
        if r is s:
            # A "readable" socket is ready to accept a connection
            connection, client_address = r.accept()
            print '    connection from', client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection
