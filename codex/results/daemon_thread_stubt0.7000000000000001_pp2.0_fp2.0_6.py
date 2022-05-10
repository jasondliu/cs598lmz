import sys, threading

def run():
    """
        Run the server.
    """

    if(len(sys.argv) < 2):
        print("Usage: python3.4 Server.py <port>")
        return

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = ('localhost', int(sys.argv[1]))
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                if data:
                    print('received {!r}'.format(data))
                    connection.sendall(data
