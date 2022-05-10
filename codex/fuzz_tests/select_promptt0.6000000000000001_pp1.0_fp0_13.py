import select
# Test select.select()

import socket
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'This is the message. It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        r, w, e = select.select([sock], [], [])
        if len(w) > 0:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
