import select
# Test select.select()
# select(rlist, wlist, xlist[, timeout]) -> (rlist, wlist, xlist)'''

import socket
import sys
import queue

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

# Sockets from which we expect to read
inputs = [sock]

# Sockets to which we expect to write
outputs = []

# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:
    # Wait for at least one of the sockets to be ready for processing
    print("\nwaiting for the next event")
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    # Handle inputs
    for s in readable:
       
