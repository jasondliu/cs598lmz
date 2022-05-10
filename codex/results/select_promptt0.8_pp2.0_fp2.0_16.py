import select
# Test select.select()

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen(5)

# Accept connections from outside
(client_socket, address) = server_socket.accept()

# Now do something with the client_socket
# In this case, we'll pretend this is a threaded server
while True:

    # Wait for input from client socket, server socket
    inputready,outputready,exceptready = select.select([client_socket, server_socket],[],[])

    for s in inputready:

        if s == server_socket:
            # Handle the server socket
            (client_socket, address) = server_socket.accept()
            print "Client socket created"

        elif s == client_socket:
            # Handle client socket
            data = s.recv(512)
            if data:
                print "Client
