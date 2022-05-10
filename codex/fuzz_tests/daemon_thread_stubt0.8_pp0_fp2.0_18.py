import sys, threading

def run():
    # Create a TCP/IP socket
    server_address = ('192.168.43.59', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('192.168.43.59', 10000)
    print('starting up on %s port %s' % server_address)
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
                data_l = []
                data = connection.recv(1024)
                while data:
                    data_l.append(data)
                    data = connection.recv(1024)
                cmd_string = b''.join(data_l)
                print(cmd_string)
