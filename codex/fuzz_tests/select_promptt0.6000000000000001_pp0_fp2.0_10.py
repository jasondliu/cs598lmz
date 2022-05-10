import select
# Test select.select()
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        # Wait for up to 1 second for a chunk of data
        ready = select.select([sock], [], [], 1)
        if ready[0]:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))
        else:
            print('waiting for
