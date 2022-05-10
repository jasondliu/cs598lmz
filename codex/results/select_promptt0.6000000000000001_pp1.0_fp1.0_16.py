import select
# Test select.select
# A simple echo server

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

# Wait for a connection
print('waiting for a connection')
connection, client_address = sock.accept()

try:
    print('connection from', client_address)

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(16)
        print('received {!r}'.format(data))
        if data:
            print('sending data back to the client')
            connection.sendall(data)
        else:
            print('no data from', client_address)
            break

finally:
    # Clean up the connection
    connection.close()
